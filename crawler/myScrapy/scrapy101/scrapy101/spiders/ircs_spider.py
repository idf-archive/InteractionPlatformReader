from scrapy.selector import Selector
from scrapy101.items import QuestionAndAnswer

__author__ = 'Danyang'

from scrapy.spider import Spider



class IrcsSpider(Spider):
    name = 'ircs'
    allowed_domains = ['http://ircs.p5w.net/']
    start_urls = ['http://ircs.p5w.net/ircs/topicInteraction/bbs.do?rid=8659']
    # rules = [Rule(SgmlLinkExtractor(allow=['/bbs.do?rid=d+']), 'parse_torrent')]


    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//td')

        # sel.xpath('//div[@id="show_q_r"]//table')
        items = []
        for site in sites:
            # title = site.xpath('a/text()').extract()
            # link = site.xpath('a/@href').extract()
            # desc = site.xpath('text()').extract()
            # print "------ ",
            # print title, link, desc
            item = QuestionAndAnswer()
            style_question = "padding:5px 25px 5px 20px; width:520px; background:#F0F0F0;border-top:solid 1px #ffffff;border-right:solid 1px #ffffff; border-bottom:solid 1px #ffffff; line-height:22px;word-wrap: break-word;"
            item['question'] = site.xpath('[@class="guest"]').extract()
            # item['answer'] = site.xpath().extract()
            items.append(item)
        return items