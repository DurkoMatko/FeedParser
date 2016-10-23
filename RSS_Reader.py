import feedparser    #parsing url
import datetime         #limiting articles just to new ones
from dateutil import parser,tz      #cast date


class RSS_Reader:
   feed_url = ""
   feedData = ""


   def __init__(self,feed_url):
      self.feed_url = feed_url

# Parse the feed from URL
   def parseFeed(self):
      print self.feed_url
      self.feedData = feedparser.parse(self.feed_url)
      print "Parsing " + self.feedData.feed.title + " - " + self.feedData.feed.subtitle

   def filterNewArticles(self):

      #yesterday's date needed to limit returned articles
      yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
      yesterday = datetime.datetime(yesterday.year, yesterday.month, yesterday.day, 20, 00, 00)

      articleList = []
      for item in self.feedData['items']:
         dt = parser.parse(item.published)      #parse unicode to datatime format
         dt = dt.astimezone(tz.tzutc())         #set it to my timezone perspective
         if(yesterday < datetime.datetime(dt.year,dt.month,dt.day,dt.hour,dt.minute,dt.second)):      #compare yesterday and article title in no-aware timezone datatime format
            articleList.append((item.link,item.title,item.description))
            
      return articleList


