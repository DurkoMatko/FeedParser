# FeedParser

Parses feeds from URLs specified in ParserSettings.xml and sends new articles to mail address (addresses are in MailSender class)<br>

To automate this process in ubuntu



```shell
sudo crontab –e

```

After crontab opens, add this line to add job which will run the script at 8pm everyday

```shell
0 20 * * * python $PATH_TO_FOLDER/parser.y

```

####Used Modules

* <b> smtplib </b>- to send mail
* <b>email </b> - MIMEText to create html version of mail text
* <b> imaplib </b> - to delete mail from Sent folder
* <b> feedparser </b> - parse the URL feed
* <b> xml.dom.minidom </b> - parsing XML to read settings
* <b> datetime </b> - time comparison
* <b> sys </b> - UTF-8 encoding


