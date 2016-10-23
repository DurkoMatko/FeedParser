from xml.dom import minidom      #get parse settings - lastDate, URLs

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

