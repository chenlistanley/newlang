import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = 'rent'
    start_urls = []
    for k in [7,85,108,117,118,142,143]:
        start_urls.append(str("https://www.shichengbbs.com/c15?area_id=%s" %k))
        start_urls.append(str("https://www.shichengzufang.com/c2?area_id=%s" %k))
        start_urls.append(str("https://www.sgyuan.com/c15?area_id=%s" %k))
    
    for k in range(1,1):
        start_urls.append(str("https://www.shichengbbs.com/c15?category2_id=321&page=%s" %k))
        start_urls.append(str("https://www.shichengzufang.com/c2?category2_id=321&page=%s" %k))
        start_urls.append(str("https://www.sgyuan.com/c15?category2_id=321&page=%s" %k))

    titles = []

    def parse(self, response):
        for quote in response.css('.info-list div'):
            title = quote.css(".title ::text").get()
            money = quote.css(".money ::text").get()
            link = quote.css(".title ::attr(href)").get()

            if not title or title in self.titles or self.findWord(title, '女','搭','隔','no more','已经出租','想租', '求租'):
                continue
            if not money:
                continue

            price = re.search('\\d+', money).group()
            if price and int(price) in range(400,601):
                self.titles.append(title)
                yield {
                    'amount': money,
                    'title':  str("<a href='%s' target='_blank'>%s </a>" %(link, title)),
                }

    def findWord(self, text, *words):
        for k in words:
            if text.find(k) != -1:
                return True
        return False