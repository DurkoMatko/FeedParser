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