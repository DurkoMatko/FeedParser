# -*- coding: utf-8 -*-

import sys
import os					#getting the path to the directory
import ConfigParser        #parsing config file
from Classes.SettingsReader import SettingsReader
from Classes.MailSender import MailSender

reload(sys)
sys.setdefaultencoding('utf8')

#create xml reader class and get feed URLs to be crawled
def main(argv):
	settingsReader = SettingsReader(os.path.dirname(os.path.abspath(__file__)) + "/ParserSettings.xml")
	settingsReader.parseXML()
	urlList = settingsReader.getFeedURLs()
	lastDate = settingsReader.getLastDate()

	mailsender = MailSender()
	mailsender.sendMail(urlList,lastDate)


if __name__ == "__main__":
    main(sys.argv)



#www.mmajunkie.com/news/rss
#http://www.reddit.com/r/python/.rss