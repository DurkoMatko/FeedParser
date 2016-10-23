# -*- coding: utf-8 -*-

import feedparser		#parsing url
import sys				#encoding
import datetime			#limiting articles just to new ones
from dateutil import parser,tz		#cast date
from xml.dom import minidom		#get parse settings - lastDate, URLs

reload(sys)
sys.setdefaultencoding('utf8')

xmldoc = minidom.parse('/home/martin/Documents/Python_Crawler/ParserSettings.xml')
urls = xmldoc.getElementsByTagName('urls')[0]
urlList = urls.getElementsByTagName("url")

for url in urlList:
	print url.firstChild.data


# Parse the feed from URL
feedData = feedparser.parse('http://www.sherdog.com/rss/news.xml')
print "Parsing " + feedData.feed.title + " - " + feedData.feed.subtitle

#yesterday's date needed to limit returned articles
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
yesterday = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 20, 00, 00)

for item in feedData['items']:
	dt = parser.parse(item.published)		#parse unicode to datatime format
	dt = dt.astimezone(tz.tzutc())			#set it to my timezone perspective - 
	if(yesterday < datetime.datetime(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)):		#compare yesterday and article title in no-aware timezone datatime format
		print item.title
		print item.link


#www.mmajunkie.com/news/rss
#http://www.reddit.com/r/python/.rss