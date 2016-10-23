# -*- coding: utf-8 -*-

import sys				#encoding
import time				#time.sleep
from SettingsReader import SettingsReader
from RSS_Reader import RSS_Reader
from MailSender import MailSender


reload(sys)
sys.setdefaultencoding('utf8')

#create xml reader class and get feed URLs to be crawled
settingsReader = SettingsReader('/home/martin/Documents/Python_Crawler/ParserSettings.xml')
settingsReader.parseXML()
urlList = settingsReader.getFeedURLs()

mailsender = MailSender()
msg=""
#for each URL specified in config settings parse feed and send mail about new articles
for url in urlList:
	#rss feed parsing
	rssReader = RSS_Reader(url.firstChild.data)
	rssReader.parseFeed()
	articleList = rssReader.filterNewArticles()			#articleList is triple of (link,title,description)

	for (link,title,description) in articleList:
         msg = msg + title + ':\n' + description + '\n(' + link + ') \n\n\n'

	#sending mail


mailsender.sendMail(url.firstChild.data,msg)








#www.mmajunkie.com/news/rss
#http://www.reddit.com/r/python/.rss