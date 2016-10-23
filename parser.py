# -*- coding: utf-8 -*-

from SettingsReader import SettingsReader
from MailSender import MailSender


#create xml reader class and get feed URLs to be crawled
settingsReader = SettingsReader('/home/martin/Documents/Python_Crawler/ParserSettings.xml')
settingsReader.parseXML()
urlList = settingsReader.getFeedURLs()

mailsender = MailSender()
mailsender.sendMail(urlList)








#www.mmajunkie.com/news/rss
#http://www.reddit.com/r/python/.rss