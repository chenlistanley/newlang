import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'mao'
    start_urls = []
    for k in range(44, 64):
    	url = str('http://www.txshuku.la/html/1063_1012%s.html' %k)
    	start_urls.append(url)

    def parse(self, response):
        for quote in response.css('.contentbox'):
            yield {
                'text': quote.get()
            }

