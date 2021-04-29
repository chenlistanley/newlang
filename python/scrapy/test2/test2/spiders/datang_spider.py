import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = 'datang'
    start_urls = []
    url = 'https://xm.lianjia.com/ershoufang/datangshijia'
    start_urls.append(url)
    for k in range(2,5):
        start_urls.append(str('%s/pg%s' %(url,k)))

    def parse(self, response):
        for quote in response.css('.sellListContent li'):
            title = quote.css(".title ::text").get()
            link = quote.css(".title ::attr(href)").get()
            totalPrice = quote.css(".totalPrice ::text").get()
            unitPrice = quote.css(".unitPrice ::text").get()
            houseInfo = quote.css(".houseInfo ::text").get()

            price = re.search("\\d+", unitPrice).group()

            # if '大唐世家' not in title:
            #     continue
            if houseInfo[0] not in ('3'):
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
               
