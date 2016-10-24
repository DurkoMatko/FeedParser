from xml.dom import minidom      #get parse settings - lastDate, URLs
import datetime                  #datetime.datetime.now()

class SettingsReader:
   filename = ""
   xmldoc = ""


   def __init__(self,filename):
      self.filename = filename

   def parseXML(self):
      self.xmldoc = minidom.parse(self.filename)

   def getFeedURLs(self):
      urls = self.xmldoc.getElementsByTagName('urls')[0]
      urlList = urls.getElementsByTagName("url")
      return urlList

   def getLastDate(self):
      lastDate = self.xmldoc.getElementsByTagName("lastDate")[0]
      oldLastDate = lastDate.firstChild.data
      lastDate.firstChild.replaceWholeText(datetime.datetime.now())

      with open(self.filename,'w') as f:
         f.write(self.xmldoc.toxml())

      return oldLastDate


