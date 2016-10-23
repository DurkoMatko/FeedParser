# -*- coding: utf-8 -*-

import sys           #encoding
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from RSS_Reader import RSS_Reader

reload(sys)
sys.setdefaultencoding('utf8')

class MailSender:
   to=""
   gmail_user=""
   gmail_pwd=""
   smtpserver=""


   def __init__(self):
      #specify acounts
      self.to = 'nitramdurcek@gmail.com'
      self.gmail_user = 'nitramdurcek@gmail.com'
      self.gmail_pwd = 'Pipkon$viem59'
      self.smtpserver = smtplib.SMTP("smtp.gmail.com",587)
      self.login()

   def login(self):
      self.smtpserver.ehlo()
      self.smtpserver.starttls()
      self.smtpserver.ehlo
      self.smtpserver.login(self.gmail_user, self.gmail_pwd)

   def sendMail(self,urlList):
      msg = self.createMessage(urlList)
      self.smtpserver.sendmail(self.gmail_user, self.to, msg.as_string())
      print 'done!'
      self.smtpserver.close()
      
   def createMessage(self,urlList):
      # Create message container - the correct MIME type is multipart/alternative.
      msg = MIMEMultipart('alternative')
      msg['Subject'] = "html test"
      msg['From'] = self.gmail_user
      msg['To'] = self.to

      text = "\n There are some new articles for you to read on Sherdog.com\n\n"
      html = """<html><head></head>
                  <body>
                     <h2><br> There are some new articles for you to read on Sherdog.com <br><br></h2>"""

      #for each URL specified in config settings parse feed and send mail about new articles
      for url in urlList:
         #rss feed parsing
         rssReader = RSS_Reader(url.firstChild.data)
         rssReader.parseFeed()
         articleList = rssReader.filterNewArticles()        #articleList is triple of (link,title,description)

         #add each new article to both text and html form
         for (link,title,description) in articleList:
               text = text + title + ':\n' + description + '\n(' + link + ') \n\n\n'
               html = html + """<b><font size="3">""" + title + """</font></b><br>""" + description + """<br>(""" + link + """)<br><br><br>"""


      html = html + """</body></html>"""
      part1 = MIMEText(text, 'plain','utf-8')
      part2 = MIMEText(html, 'html','utf-8')

      msg.attach(part1)
      msg.attach(part2)

      return msg

