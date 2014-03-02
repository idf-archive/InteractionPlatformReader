from scrapy.selector import Selector
from scrapy101.items import DmozItem

__author__ = 'Danyang'

from scrapy.spider import Spider


class DmozSpider(Spider):
    name = "dmoz"
    allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
        "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        # filename = response.url.split("/")[-2] # just for your internal file names
        # open(filename, 'wb').write(response.body)

        sel = Selector(response)
        sites = sel.xpath('//ul/li')
        items = []
        for site in sites:
            # title = site.xpath('a/text()').extract()
            # link = site.xpath('a/@href').extract()
            # desc = site.xpath('text()').extract()
            # print "------ ",
            # print title, link, desc
            item = DmozItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()').extract()
            items.append(item)
        return items