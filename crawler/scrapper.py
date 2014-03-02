from cssselect import Selector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule

__author__ = 'Danyang'
from scrapy.item import Item, Field


class QuestionAndAnswer(Item):
    question = Field()
    answer = Field()


class IrcsSpider(CrawlSpider):
    name = 'IRCS'
    allowed_domains = ['http://ircs.p5w.net/']
    start_urls = ['http://ircs.p5w.net/ircs/topicInteraction/']
    rules = [Rule(SgmlLinkExtractor(allow=['/bbs.do?rid=d+']), 'parse_torrent')]

    def parse_q_and_a(self, response):
        sel = Selector(response)
        target = QuestionAndAnswer()
        target['url'] = response.url
        target['name'] = sel.xpath("//h1/text()").extract()
        target['description'] = sel.xpath("//div[@id='description']").extract()
        target['size'] = sel.xpath("//div[@id='info-left']/p[2]/text()[2]").extract()
        return target