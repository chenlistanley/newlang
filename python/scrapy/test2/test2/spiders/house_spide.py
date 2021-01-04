import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'house'
    start_urls = [
        'https://xm.anjuke.com/sale/rd1/?kw=%e9%9b%aa%e6%a2%a8%e6%98%9f%e5%85%89&pi=baidu-cpc-xm-lp2&kwid=61869307668&bd_vid=7944333559217886248',
    ]

    def parse(self, response):
        for quote in response.css('#houselist-mod-new'):
            yield {
                'text': quote.get(),
            }
