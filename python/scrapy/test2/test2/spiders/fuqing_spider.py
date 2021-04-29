import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = 'fuqing'
    url = 'https://fz.lianjia.com/ershoufang/fuqingshi'
    start_urls = []
    start_urls.append(url)
    for k in range(2,23):
        start_urls.append(str('%s/pg%s' %(url,k)))

    def parse(self, response):
        for quote in response.css('.sellListContent li'):
            title = quote.css(".title ::text").get()
            link = quote.css(".title ::attr(href)").get()
            totalPrice = quote.css(".totalPrice ::text").get()
            unitPrice = quote.css(".unitPrice ::text").get()
            houseInfo = quote.css(".houseInfo ::text").get()

            price = re.search("\\d+", unitPrice).group()

            if float(totalPrice) > 80:
                continue
            if houseInfo.find('车位') != -1:
                continue
            if int(houseInfo[0]) < 2:
                continue
            if int(price) > 20000:
                continue
           
            yield {
                'totalPrice': totalPrice,
                'unitPrice': unitPrice,
                'houseInfo': houseInfo,
                'title':  str("<a href='%s' target='_blank'>%s </a>" %(link, title)),
            }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
               
