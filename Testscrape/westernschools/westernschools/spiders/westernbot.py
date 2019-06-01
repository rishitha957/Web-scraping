# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 10:03:26 2019

@author: rishitha
"""
import scrapy


class WesternbotSpider(scrapy.Spider):
    name = 'westernbot'
    #allowed_domains = ['https://www.westernschools.com/course-library/']
    start_urls = ['https://www.westernschools.com/course-library//']

    def parse(self, response):
        link = response.xpath("//a[@class='mega-menu-link']/@href").extract()
        for i in range(19,29):
            url = link[i]
            yield scrapy.Request(url,callback=self.parse1)
    
    def parse1(self,response):
        url1 = 'https://www.westernschools.com'
        links1 = response.xpath("//div[@class='course-container']/a[@class='course-name course-link']/@href").extract()
        self.urllist = []
        for i in links1:
            url = url1 + i
            self.urllist.append(url)
            yield scrapy.Request(url,callback=self.parse2)
    
    def parse2(self,response):
        list1 = []
        list1.append(self.urllist)
        name = response.xpath("//div[@class='constraint clearfix']/h1/text()").extract()
        list1.append(name)
        details = response.xpath("//div[@class='constraint']/div/p/b/text()").extract()
        str1 = details[0]
        Release_date = []
        Release_date.append(str1[15:])
        list1.append(Release_date)
        str1 = details[1]
        Expiry_date = []
        Expiry_date.append(str1[18:])
        list1.append(Expiry_date)
        str1 = details[2]
        hours = []
        hours.append(str1)
        list1.append(hours)
        para = []
        str1 = response.xpath("//div[@class='constraint']/div/p/text()").extract_first()
        para.append(str1)
        list1.append(para)
        for i in range(len(name)):
            yield{
                'name':list1[1][i],
                'link':list1[0][i],
                'release_date':list1[2][i],
                'expiry_date':list1[3][i],
                'hours':list1[4][i],
                'para':list1[5][i],
            }
        