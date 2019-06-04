# -*- coding: utf-8 -*-
import scrapy


class IssueSpider(scrapy.Spider):
    name = 'issubot'
    #allowed_domains = ['www.issu.com']
    start_urls = ['http://directory.imagorelationships.org/find-a-therapist/results/?pg=1']

    def parse(self, response):
        url1 = 'http://directory.imagorelationships.org/find-a-therapist/results/?pg='
        for i in range(1,64):
            url = url1 + str(i);
            yield scrapy.Request(url,callback=self.parse1)
    
    def parse1(self,response):
        l1 = []
        name = response.css(".resultInfo a::text").extract()
        l1.append(name)
        number1 = response.css(".phoneNum::text").extract()
        number = []
        for i in range(0,len(number1),2):
            number1[i] = number1[i].replace("\r","")
            number1[i] = number1[i].replace("\n","")
            number1[i] = number1[i].strip(" ")
            number1[i] = number1[i].replace("T: ","")
            number.append(number1[i])
        l1.append(number)
        email =  response.css(".emailAdr a::text").extract()
        l1.append(email)
        address1 = response.css(".address::text").extract()
        address  = []
        for i in range(0,len(address1),2):
            str1 = address1[i].replace("\n","")
            str1 = str1.replace("\r","")
            str1 = str1.strip(" ")
            str2 = ""
            if(i+1<len(address1)):
                str2 = address1[i+1].replace("\n","")
                str2 = str2.replace("\r","")
                str2 = str2.strip(" ")
            str3 = str1+str2
            address.append(str3)
        l1.append(address)
        
        for i in range(len(name)):
            yield{
                'name':l1[0][i],
                'number':l1[1][i],
                'email':l1[2][i],
                'address':l1[3][i],
            }
        
        
        
            
            
            
