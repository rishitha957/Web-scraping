# -*- coding: utf-8 -*-

"""
Created on Sat May 25 14:18:23 2019

@author: rishitha 
"""
import scrapy
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from bs4 import BeautifulSoup


class AacpbotSpider(scrapy.Spider):
    name = 'aacpbot'
    allowed_domains = ['www.aacp.org.uk']
    start_urls = ['http://www.aacp.org.uk/']

    def __init__(self):
        driver = webdriver.Firefox()
       
        
    def parse(self, response):
        driver.get('https://www.aacp.org.uk/search?loc=Peterborough&distance=5')
        res = driver.execute_script("return document.documentElement.outerHTML")
        res1 = driver.find_elements_by_xpath("//div/img[@src='/modules/main/images/marker_blue.gif']/map/area")
        for item in res1:
            item.click().perform()
            practitioner = driver.find_element_by_id("tdPractitioner")
            print("practioner:"+practitioner)
            if(len(practitioner)==0):
                print("Error occured")
            soup = BeautifulSoup(res, 'lxml')
        pass
