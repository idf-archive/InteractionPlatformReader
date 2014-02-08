# Potential Gateways:
# http://finance.yahoo.com/q/h?s=GOOG&t=2013-10-07
# Special topic
# http://search1.bloomberg.com/search?content_type=news&max_age=0&page=1&q=GOOG&sort=1 # till 18 Apr 2013
# http://www.reuters.com/finance/stocks/companyNews?symbol=GOOG.O&date=01072013
# http://www.investors.com/search/searchresults.aspx?No=100&N=4294967251&Nr=AND(Content+Type%3aArticles%2cSource%3aCMS%2cSymbol%3aGOOG)&Ns=P_CreatedDate_unixts|1&module=InTheNews
# 
from goose import Goose 
import urllib2
urls = [
	'http://www.newyorker.com/online/blogs/currency/2014/02/whats-the-point-of-city-logos.html',
	'http://news.investors.com/020714-689410-facebook-jokes-on-anniversary.htm?ven=yahoocp&src=aurlled&ven=yahoo',
	'http://finance.yahoo.com/blogs/talking-numbers/these-two-charts-say-sell-this-highflying-stock-230649770.html',
	'http://www.newyorker.com/online/blogs/currency/2014/02/whats-the-point-of-city-logos.html',
	'http://www.engadget.com/2014/02/07/edit-your-facebook-look-back-video/?ncid=rss_truncated',
	'http://www.thestreet.com/_yahoo/video/12317830/time-to-get-aggressive-on-williams-sonoma-hollyfrontier.html?cm_ven=YAHOOV&cm_cat=FREE&cm_ite=NA&s=1',
	'http://www.usatoday.com/story/tech/2014/02/07/week-tech-microsoft-facebook-twitter/5284443/',
	'http://www.wired.com/wiredenterprise/2014/02/facebook-hacks/?mbid=synd_yfinance',
	]
g = Goose()
text_file = open("Output.txt", "w")
for url in urls:
	article = g.extract(url=url)

	#article_html = urllib2.urlopen(url)
	#article.publish_date = article_html.headers.get("last-modified", None)
	#not desirable

	text_file.write("title: %s\n"%article.title)
	#text_file.write("datetime: %s\n"%article.publish_date)
	text_file.write("body: %s\n"%article.cleaned_text[:-1].encode("utf-8"))
	text_file.write("==============================================\n")
text_file.close()