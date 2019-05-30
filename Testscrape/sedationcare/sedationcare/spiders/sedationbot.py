# -*- coding: utf-8 -*-
"""
Created on Thu May 30 14:31:03 2019

@author: rishitha
"""
import scrapy


class SedationbotSpider(scrapy.Spider):
    name = 'sedationbot'
    #allowed_domains = ['https://www.sedationcare.com/UserSearch?distance[postal_code]=maryland']
    start_urls = ["https://www.sedationcare.com/UserSearch?distance[postal_code]=maryland&distance[country]=us&distance[search_distance]=100&distance[search_units]=mile"]

    def parse(self, response):
        url1 = "https://www.sedationcare.com/UserSearch?distance[postal_code]=maryland&distance[country]=us&distance[search_distance]=100&distance[search_units]=mile"
        list1 = ['Alabama',
                'Alaska',
                'Arizona',
                'Arkansas',
                'California',
                'Colorado',
                'Connecticut',
                'Delaware',
                'Florida',
                'Georgia',
                'Hawaii',
                'Idaho',
                'Illinois',
                'Indiana',
                'Iowa',
                'Kansas',
                'Kentucky',
                'Louisiana',
                'Maine',
                'Maryland',
                'Massachusetts',
                'Michigan',
                'Minnesota',
                'Mississippi',
                'Missouri',
                'Montana',
                'Nebraska',
                'Nevada',
                'New%20Hampshire',
                'New%20Jersey',
                'New%20Mexico',
                'New%20York',
                'North%20Carolina',
                'North%20Dakota',
                'Ohio',
                'Oklahoma',
                'Oregon',
                'Pennsylvania',
                'Rhode%20Island',
                'South%20Carolina',
                'South%20Dakota',
                'Tennessee',
                'Texas',
                'Utah',
                'Vermont',
                'Virginia',
                'Washington',
                'West%20Virginia',
                'Wisconsin',
                'Wyoming',]
        for state in list1:
            url = url1[:62]+state+url1[70:]
            yield scrapy.Request(url,callback=self.parse1)
    
    def parse1(self,response):
        list2 = []
        name = response.css(".doctor-name::text").extract()
        for i in range(len(name)):
            name[i] = name[i].replace("\n","")
            name[i] = name[i].replace("\t","")
        list2.append(name)
        address1 = response.css(".doctor-address::text").extract()
        self.j = 0
        address = []
        for i in range(0,len(address1),3):
            str1 = address1[i]
            str1 = str1 + address1[i+1]
            str1 = str1 + address1[i+2]
            str1 = str1.replace("\n","")
            str1 = str1.replace("\t","")
            str1 = str1.replace("<br>","")
            address.append(str1)
        list2.append(address)
        number = response.css(".doctor-number::text").extract()
        list2.append(number)
        email = response.css(".doctor-email a::attr(href)").extract()
        for i in range(len(email)):
            email[i] = email[i].replace('mailto:','')
        list2.append(email)
        
        for i in range(len(name)):
            yield{
                'name':list2[0][i],
                'address':list2[1][i],
                'number':list2[2][i],
                'email':list2[3][i],
            }
            
