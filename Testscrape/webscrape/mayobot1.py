# -*- coding: utf-8 -*-
"""
Created on Thu May 23 11:25:45 2019

@author: rishi
"""

import scrapy


class practice(scrapy.Spider):
  name = "startname"
  allowed_domain = ["ce.mayo.edu"]
  start_urls = ["http://ce.mayo.edu/?_ga=2.234396830.1635211149.1531979045-1996999075.1531979045"]
  def parse(self, response):
      for b in response.xpath('//div[@class="linkitem"]/text()').extract():
          yield scrapy.Request(b, callback = self.single_info)
          
      for href in response.xpath('//div[@class="col"]/a/@href').extract():
          print("https://ce.mayo.edu/"+href)
          yield scrapy.Request("https://ce.mayo.edu/"+href, callback = self.spec_info)
  def spec_info(self, response):
      for url in response.xpath('//tr/td/a/@href').extract():
          print(url)
          yield scrapy.Request("https://ce.mayo.edu/"+url, callback = self.single_info)

  def single_info(self, response):
      sin_info = {}
      sin_with_info = []
      sin_info['speciality'] = [b]
      sin_info['link'] = "http://ce.mayo.edu/"+str(response.xpath('//div[@class="breadcrumb"]/a[3]/@href').extract())
      sin_info['title'] = response.xpath('//div[@class="field-items"]/div/h1/text()').extract()
      sin_info['startdate'] = response.xpath('//span[@class="date-display-range"]/span[@class="date-display-start"]/text()').extract()
      sin_info['enddate'] =  response.xpath('//span[@class="date-display-range"]/span[@class="date-display-end"]/text()').extract()
      sin_info['fee'] = response.xpath('//div[@class="field-item"]/strong/text()').extract()
      sin_info['location'] = response.xpath('//div[@class="field-items"]/div[@class="field-item even"]/text()').extract()
      sin_with_info.append(sin_info)
      for sin_info in sin_with_info:
          yield {
                   'title' :sin_info['title'],
                   'Speciality' :sin_info['speciality'],
                   'Startdate':sin_info['startdate'],
                   'Enddate':sin_info['enddate'],
                   'Fee':sin_info['fee'],
                   'Location':sin_info['location'],
                   'Links':sin_info['link'],
                   }
          
execute(['scrapy','crawl','startname'])

