import scrapy,re

class QuotesSpider(scrapy.Spider):
    name = 'bbs'
    start_urls = []
    for k in range(5):
        start_urls.append(str("https://bbs.sgcn.org/forum-197-%s.html" %(k+1)))
    cache={}

    def parse(self, response):
        for quote in response.css('#threadlisttableid tbody'):
            title = quote.css(".s.xst::text").get()
            link = quote.css(".s.xst::attr(href)").get()
            if not title or not link:
                continue
            if self.findWord(title, '已', '收', '充电器', '内存条', '转换头') or not self.findWord(title, 'Mac', '笔记本'):
                continue
            self.cache.update({title:link})
            yield response.follow(link, self.parse2)

    def parse2(self, response):
        title=response.css('#thread_subject::text').get()
        for quote in response.css('.cgtl.mbm tbody tr'):
            itemName = quote.css("th::text").get()
            itemValue = quote.css("td::text").get()
            if not itemName or not self.findWord(itemName, '价格'):
                continue
            price=re.sub("\\D", "", itemValue)
            price=int(price)
            if price >= 300 or price < 40:
                continue
            yield {
                'title': str("<a href='%s' target='_blank'>%s</a>" %(self.cache.get(title), title)),
                'price': price,
            }

    def findWord(self, text, *words):
        for k in words:
            if text.find(k) != -1:
                return True
        return False