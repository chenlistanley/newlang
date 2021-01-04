import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'dict'
    start_urls = [
        'http://dict.cn/strong',
    ]

    def parse(self, response):
        for quote in response.css('div.word'):
            yield {
                'sound': quote.css('div.phonetic span bdo::text').get(),
                'translation': quote.css('div ul li strong::text').get(),
            }
