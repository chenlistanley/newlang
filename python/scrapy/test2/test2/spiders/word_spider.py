import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = 'word'
    start_urls = ['https://kaoyan.koolearn.com/20190131/1035624.html']
    for k in range(40, 51):
        start_urls.append(str('https://kaoyan.koolearn.com/20190121/10349%s.html' %k))

    def parse(self, response):
        for quote in response.css('.xqy_core_text p'):
            a = quote.xpath('text()').get()
            yield {
                'word':  a,
            }