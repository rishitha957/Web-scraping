# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 09:43:02 2019

@author: rishi
"""

import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import bs4

class BlsbotSpider(scrapy.Spider):
    name = 'morebot'
    #allowed_domains = ['https://www.lifesavered.com/classes/bls-training']
    start_urls = ['https://www.lifesavered.com/classes']
    
    def __init__(self):
        self.driver = webdriver.Firefox()
        
    def parse(self, response):
        #driver = webdriver.Firefox()
        url1 =  response.xpath("//a[@class='button']/@href").extract()
        for url in url1:
            url_1 = 'https://www.lifesavered.com'+url
            self.driver.get(url_1)
            res = self.driver.execute_script("return document.documentElement.outerHTML")
            #url1 = res.xpath('//ul/li/a/@href').extract()
            soup = bs4.BeautifulSoup(res,'lxml')
            
            for i in soup.find_all('div', {"class":"button-container"}):
                for b in i.findAll('a',{"class":"button red"}):
                    url = b.get('href')
                    yield scrapy.Request(url,callback=self.parse1)
            
    def parse1(self,response):
        list1 = []
        date_time = response.css('#maincontent_datelocRow tr:nth-child(1) td::text').extract()
        for i in range(len(date_time)):
            date_time[i] = date_time[i].replace("\r","")
            date_time[i] = date_time[i].replace("\n","")
            date_time[i] = date_time[i].strip(" ")
        
        list1.append(date_time)
        location = response.css('tr+ tr td::text').extract()
        for i in range(len(location)):
            location[i] = location[i].replace("\r","")
            location[i] = location[i].replace("\n","")
            location[i] = location[i].strip(" ")
        list1.append(location)  
        classprice = response.css('#maincontent_classpricerow td::text').extract()
        for i in range(len(classprice)):
            classprice[i] = classprice[i].replace("\r","")
            classprice[i] = classprice[i].replace("\n","")
            classprice[i] = classprice[i].strip(" ")
            
        name = response.css(".enrtabletitle::text").extract()
        for i in range(len(name)):
            name[i] = name[i].replace("\r","")
            name[i] = name[i].replace("\n","")
            name[i] = name[i].strip(" ")
        list1.append(classprice)
        list1.append(name)
        for i in range(len(date_time)):
            yield{
                'name':list1[3][i],
                'date_time':list1[0][i],
                'location':list1[1][i],
                'classprice':list1[2][i],
            }