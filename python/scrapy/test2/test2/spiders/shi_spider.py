import scrapy,re

class QuotesSpider(scrapy.Spider):
    name = 'shi'
    start_urls = []
    start_urls.append("https://www.shichengbbs.com/c206")
    start_urls.append("https://www.singxin.com/c39")
    start_urls.append('https://www.sgyuan.com/c39')
 
    def parse(self, response):
        for quote in response.css('.media.pb-2.pt-2'):
            title = quote.css(".title::text").get()
            link = quote.css(".title::attr(href)").get()
            price = quote.css(".money::text").get()
            if not title or not link or not price:
                continue
            if self.findWord(title, '已', '收', '充电器', '内存条', '转换头', '维修', '安装', '包') or not self.findWord(title, 'Mac', '笔记本', '电脑'):
                continue
            price = price.replace("S$", "").strip()
            price=re.sub("\\D", "", price)
            price=int(price)
            if price >= 300 or price < 40:
                continue
            yield {
                'title': str("<a href='%s' target='_blank'>%s</a>" %(link, title)),
                'price': price,
            }

    def findWord(self, text, *words):
        for k in words:
            if text.find(k) != -1:
                return True
        return False