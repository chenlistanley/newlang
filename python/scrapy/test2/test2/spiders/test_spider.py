import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'test'
    start_urls = [
        'https://www.biquge5200.cc/0_111',
    ]

    def parse(self, response):
        for quote in response.css('#list dl dd'):
            yield {
                'text': quote.css("a::text").get(),
                'link': quote.css('a::attr(href)').get(),
            }
