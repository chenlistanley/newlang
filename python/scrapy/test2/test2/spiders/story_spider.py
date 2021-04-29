import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'story'
    start_urls = [
        'http://www.xbiquge.la/0/10'
    ]

    def parse(self, response):
        quote = response.css('#list dl dd')[-1]
        yield {
            'text': quote.css("a::text").get(),
            'link': quote.css('a::attr(href)').get(),
        }
        next_page = quote.css('a::attr(href)').get()
        if next_page is not None:
        	yield response.follow(next_page, self.parse2)

    def parse2(self, response):
        for quote in response.css('#content'):
            yield {
                'content': quote.get(),
            }
