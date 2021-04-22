#coding:utf-8

import scrapy

class Xvideos(scrapy.Spider) :
    name = 'xvideos'
    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response) :
        
        title = response.css('title::text').extract()

        yield {'xvideostitle' : title}
