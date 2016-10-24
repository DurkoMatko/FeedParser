# -*- coding: utf-8 -*-

from SettingsReader import SettingsReader
from MailSender import MailSender

#create xml reader class and get feed URLs to be crawled
settingsReader = SettingsReader('/home/martin/Documents/Python_Crawler/ParserSettings.xml')
settingsReader.parseXML()
urlList = settingsReader.getFeedURLs()
lastDate = settingsReader.getLastDate()

mailsender = MailSender()
mailsender.sendMail(urlList,lastDate)








#www.mmajunkie.com/news/rss
#http://www.reddit.com/r/python/.rss