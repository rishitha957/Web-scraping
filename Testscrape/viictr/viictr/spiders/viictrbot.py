# -*- coding: utf-8 -*-

"""
Created on Tue May 28 12:48:44 2019

@author: rishitha
"""

import scrapy
import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from PIL import Image
import pytesseract


class ViictrbotSpider(scrapy.Spider):
    name = 'viictrbot'
    #allowed_domains = ['https://profiles.viictr.org/search/default.aspx?searchtype=people']
    start_urls = ['https://profiles.viictr.org/search/']

    def parse(self, response):
        url1 = "https://profiles.viictr.org/search/default.aspx?searchtype=people&searchfor=&exactphrase=false&perpage=100&offset=0&page=81&totalpages=93&searchrequest=A81BSfTwU3GNm4liSODkW6vB3EBYO6gz+a5TY1bFhuz1tc7ngL4Orww3064KoquGaRdozjhWRGlrnur5IbaEcMH3TeE05jmp/c7agcYTrzG/rrN5T5p39rbdUtWdCA0xO6jz/+zNo8xTen6DVgqqi0W/y1wHaBbEaTD7d+ObAfEiPSt4sYkjfpHHCVWp3IgQjZuJYkjg5FtrbjF9BEDCXidTb5mQuzDHyB9Btw8xWu2KulNUp49QuXYgzDfXM/0XsMVgFPQNiicDoJOpif4f2tJz+lXwtXBUlbMMfLafD2/FQk/vlQFoQtTytKqtEzKxt8of3H04IOI=&sortby=&sortdirection=&showcolumns=1"
        
        for i in range(1,94):
            url = url1[:121]+str(i)+url1[123:]
            yield scrapy.Request(url,callback=self.parse1)
            
    def parse1(self,response):
        link = response.xpath("//a[@class='listTableLink']/@href").extract()
        for url in link:
            yield scrapy.Request(url,callback=self.parse2)
            
    def parse2(self,response):
        list1 = []
        name = response.css(".pageTitle span::text").extract()
        list1.append(name)
        title =  response.css(".basicInfo tr:nth-child(1) span::text").extract()
        list1.append(title)
        institution = response.css("tr+ tr span::text").extract()
        list1.append(institution)
        dep1 =  response.css("#ctl00_divProfilesContentMain tr:nth-child(3) td::text").extract()
        department = []
        for i in range(0,len(dep1),3):
            department.append(dep1[i])
        list1.append(department)
        #email_l = response.css(".basicInfo img::attr(src)").extract()
        #email = []
        #for i in email_l:
            #str1 = pytesseract.image_to_string(i,lang='eng')
            #email.append(str1)
        for i in range(len(name)):
            yield{
                'name':list1[0][i],
                'title':list1[1][i],
                'institution':list1[2][i],
                'department':list1[3][i],
            }
        
        
