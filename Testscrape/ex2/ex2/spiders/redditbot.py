# -*- coding: utf-8 -*-
import scrapy


class RedditbotSpider(scrapy.Spider):
    name = 'redditbot'
    #allowed_domains = ['www.reddit.com/r']
    start_urls = ['http://quotes.toscrape.com/']
    handle_httpstatus_list = [400]
    def parse(self, response):
        #extracting the content using the css selectors
        
        quotes = response.xpath("/div[@class=row]/div/div/span/text()")
        authors = response.css('.author::text').extract()
        tags = response.css('.tag::text').extract()
       # comments = response.css('.comments::text').extract()
        
        #Give the extracted content row wise
        for item in zip(quotes,authors,tags):
            #created directory to store the scraped info
            scraped_info = {
                    'quote' : item[0],
                    'author' : item[1],
                    'tag' : item[2],
                    #'comments' :item[3],
            }
            
            #yield the scraped info
            yield scraped_info 
