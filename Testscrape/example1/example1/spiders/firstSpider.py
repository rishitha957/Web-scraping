# -*- coding: utf-8 -*-
"""
Created on Tue May 21 21:12:08 2019

@author: rishi
"""

import scrapy

class quotes_scrap(scrapy.Spider):
    name = "quotes"
    start_url = [
                'http://quotes.toscrape.com/',
            ]
    
    def parse(self,response):
        title = response.css('title::text').extract()
        yield {'titletext' : title}
        
        
