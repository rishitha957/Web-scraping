# -*- coding: utf-8 -*-

"""
Created on Sat May 25 09:12:45 2019

@author: rishi
"""

import scrapy


class BayadabotSpider(scrapy.Spider):
    name = 'bayadabot'
    #allowed_domains = ['https://education.bayada.com']
    start_urls = ["https://education.bayada.com/pediatric-practice/courses"]

    def parse(self, response):
        url1 = "https://education.bayada.com/pediatric-practice/courses"
        url2="https://education.bayada.com/pediatric-practice/courses?page="
        for i in range(6):
            self.count = i;
            if(i==0):
                url = url1
            else:
                url = url2+str(i)
            yield scrapy.Request(url,callback=self.parse1)
            
    def parse1(self,response):
        list2 = []
        
        title = response.css("td a::text").extract()
        list2.append(title)
        target_audience = response.css("td.views-field-field-custom-target-audience::text").extract()
        for i in range(len(target_audience)):
            target_audience[i] = target_audience[i].replace("\n","")
            target_audience[i]=target_audience[i].strip(" ")
        list2.append(target_audience)
        credits1 = response.css("#footable .last::text").extract()
        list2.append( credits1)
        activity_format = response.css("td.views-field-field-activity-format::text").extract()
       
        for i in range(len(activity_format)):
            activity_format[i] = activity_format[i].replace("\n","")
            activity_format[i]=activity_format[i].strip(" ")
            
        list2.append(activity_format)
        for j in range(15):
            yield{
                    "title":list2[0][j],
                    "target_audience":list2[1][j],
                    "credits":list2[2][j],
                    "activity_format":list2[3][j] 
            }
        
        
