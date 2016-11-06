# -*- coding: utf-8 -*-

import sys           #encoding
import email, imaplib      #deleting sent mails from sent folder
import smtplib
import os                  ##getting path
import ConfigParser        #parsing config file
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from Classes.RSS_Reader import RSS_Reader
from urlparse import urlparse

reload(sys)
sys.setdefaultencoding('utf8')

class MailSender:
   to=""
   gmail_user=""
   gmail_pwd=""
   smtpserver=""


   def __init__(self):
      #specify acounts
      configParser = ConfigParser.ConfigParser()
      configParser.readfp(open(os.path.dirname(os.path.abspath(__file__))+"/mailCredentials.config"))
      self.to = configParser.get('GmailConfig','to')
      self.gmail_user = configParser.get('GmailConfig','from')
      self.gmail_pwd = configParser.get('GmailConfig','from_password')
      self.smtpserver = smtplib.SMTP("smtp.gmail.com",587)
      self.login()

   def login(self):
      self.smtpserver.ehlo()
      self.smtpserver.starttls()
      self.smtpserver.ehlo
      self.smtpserver.login(self.gmail_user, self.gmail_pwd)

   def sendMail(self,urlList,lastDate):
      msg = self.createMessage(urlList,lastDate)

      #if msg is not false, then send it
      if(msg):
         self.smtpserver.sendmail(self.gmail_user, self.to, msg.as_string())
         #delete mails from sent folder - so it's only in INBOX
         self.cleanSentFolder()     

      self.smtpserver.close()

      
      
   def createMessage(self,urlList,lastDate):
      # Create message container - the correct MIME type is multipart/alternative.
      msg = MIMEMultipart('alternative')
      msg['Subject'] = "Daily feed"
      msg['From'] = self.gmail_user
      msg['To'] = self.to

      text = "\n Your daily feed is here!\n\n"
      html = """<html><head></head>
                  <body>
                     <h2><br> Your daily feed is here! <br><br></h2>"""

      #flag to detect if at least some articles are new
      newArticles = False

      #for each URL specified in config settings parse feed and send mail about new articles
      for url in urlList:
         #add URL name to mail as a title
         domain =  self.getDomainFromURL(url.firstChild.data)
         text = text + '\n\n' + domain;
         html = html + """<br><br><h3>""" + domain + """</h3><br>"""
         #rss feed parsing
         rssReader = RSS_Reader(url.firstChild.data)
         rssReader.parseFeed()
         articleList = rssReader.filterNewArticles(lastDate)        #articleList is triple of (link,title,description)

         if(len(articleList)!=0):
            newArticles = True

         #add each new article to both text and html form
         for (link,title,description) in articleList:
               text = text + title + ':\n' + description + '\n(' + link + ') \n\n\n'
               html = html + """<b><font size="3">""" + title + """</font></b><br>""" + description + """<br>(""" + link + """)<br><br><br>"""

      if(newArticles):
         html = html + """</body></html>"""
         part1 = MIMEText(text, 'plain','utf-8')
         part2 = MIMEText(html, 'html','utf-8')

         msg.attach(part1)
         msg.attach(part2)

         return msg
      else:
         return False


   def cleanSentFolder(self):
      m = imaplib.IMAP4_SSL("imap.gmail.com",993)
      m.login(self.gmail_user,self.gmail_pwd)

      # select Sent folder - name is in slovak
      status,msg = m.select('[Gmail]/Odoslan&AOk-')     

      if(status == 'OK'):
         #get all sent messages and then extract Message-ID of the newest one - not UID!
         result, data = m.uid('search', None, "ALL") # search and return uids 
         latest_email_uid = data[0].split()[-1]
         result, data = m.uid('fetch', latest_email_uid, '(RFC822)')

         if(result == 'OK'):
            splitData = data[0][0].split(" ")
            messageId = splitData[0]
            #delete message using its Message-ID
            m.store(messageId,'+FLAGS', '\\Deleted')
            m.expunge()    

      m.logout()


   def getMailIdBySubject(self,m,subject):
      result, data = m.uid('search', None, '(HEADER Subject "' + subject + '")')
      return data

   def getDomainFromURL(self,url):
      parsed_uri = urlparse( url )
      domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
      return domain

