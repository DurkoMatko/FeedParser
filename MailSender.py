import smtplib

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

   def sendMail(self,feed,msg):
      header = 'To:' + self.to + '\n' + 'From: ' + self.gmail_user + '\n' + 'Subject:' + feed + ' parsed news\n'
      msg = header + '\n There are some new articles for you to read on Sherdog.com\n\n' + msg


      self.smtpserver.sendmail(self.gmail_user, self.to, msg)
      print 'done!'
      self.smtpserver.close()
      


