import scrapy
import re


class QuotesSpider(scrapy.Spider):
    name = 'exchange'
    start_urls = ['https://zhongguoremittance.com/zh-chs/home']

    def parse(self, response):
        for quote in response.css('.elementor-element.elementor-element-08793be.elementor-widget__width-initial.elementor-widget-tablet__width-initial.elementor-widget-mobile__width-inherit.elementor-widget.elementor-widget-heading'):
            rate = quote.css("div p ::text").get()
            print(str("CNY %s" %rate))
            yield {
                'CNY': rate
            }
