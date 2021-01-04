import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'story'
    start_urls = [
        'https://www.biquge5200.cc/0_111',
    ]

    def parse(self, response):
        for quote in response.css('#list dl'):
            yield {
                'text': quote.css("dd a::text").get(),
                'link': quote.css('dd a::attr(href)').get(),
            }
            next_page = response.css('dd a::attr(href)').get()
            if next_page is not None:
            	yield response.follow(next_page, self.parse2)

    def parse2(self, response):
        for quote in response.css('#content'):
            yield {
                'content': quote.get(),
            }
