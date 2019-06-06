# -*- coding: utf-8 -*-
"""
Created on Sat May 25 15:53:49 2019

@author: rishi
"""
"""
import tabula

df = tabula.read_pdf("test.pdf", pages='all')
df2 = tabula.read_pdf("April2015.pdf")
tabula.convert_into("test.pdf", "output.csv", output_format="csv", pages='all')
tabula.convert_into_by_batch("input_directory", output_format='csv', pages='all')
"""


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import bs4

urls = 'https://www.lifesavered.com/classes/bls-training/'
driver = webdriver.Firefox()
driver.get(urls)
res = driver.execute_script("return document.documentElement.outerHTML")
#url1 = res.xpath('//ul/li/a/@href').extract()
soup = bs4.BeautifulSoup(res,'lxml')

for i in soup.find_all('div', {"class":"button-container"}):
    for b in i.findAll('a',{"class":"button red"}):
        url = b.get('href')
        print(url)
