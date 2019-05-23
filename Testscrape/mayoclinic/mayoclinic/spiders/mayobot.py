# -*- coding: utf-8 -*-
import scrapy

class MayobotSpider(scrapy.Spider):
    name = 'mayobot'
    #allowed_domains = ['https://ce.mayo.edu/?_ga=2.66847342.1743406290.1558523196-2134927995.1558523196']
    start_urls = ['https://ce.mayo.edu/?_ga=2.66847342.1743406290.1558523196-2134927995.1558523196/']
   
    def parse(self, response):
        #specialities1 = response.xpath("//div[@class='col']/a[@class='flexitem']/div[@class='linkitem']/text()").extract()
        self.dict1 = {}
        self.list1 = []
        url1 = "https://ce.mayo.edu"
        speciality_link = response.xpath('//div[@class="col"]/a[@class="flexitem"]/@href').extract()
        self.logger.info(speciality_link)
        for extension in speciality_link:
            url = url1+extension
            spec1 = response.xpath("//h1[@class='title']/text()").extract()
            self.dict1['spec'] = spec1
            self.logger.info("the url is:",url)
            response = scrapy.Request(url, callback=self.parse1)
            yield response
    def parse1(self,response):
        title1 = response.xpath("//td[@class='views-field views-field-title']/a/text()").extract()
        self.dict1['title'] = title1
        url2 = "https://ce.mayo.edu/anesthesiology/node/1595"
        link = response.xpath("//td[@class='views-field views-field-title']/a/@href").extract()
        for link in link:
            url = url2+link
            self.logger.info("The url in loop2 is:",url)
            yield scrapy.Request(url,callback=self.parse2)
    def parse2(self,response):
        startdate1 = response.xpath('//span[@class="date-display-range"]/span[@class="date-display-start"]/text()').extract()
        self.dict1['startdate']=startdate1
        enddate1 = response.xpath('//span[@class="date-display-range"]/span[@class="date-display-end"]/text()').extract()
        self.dict1['enddate'] = enddate1
        fee1 = response.xpath('//div[@class="field-item"]/strong/text()').extract()
        self.dict1['fee'] = fee1
        location1 = response.xpath('//div[@class="field-items"]/div[@class="field-item even"]/text()').extract()
        self.dict1['location'] = location1
        self.list1.append(self.dict1) 
        for dict1 in self.list1:
            yield{
                'title' : dict1['title'],
                'speciality':dict1['spec'],
                'startdate':dict1['startdate'],
                'enddate':dict1['enddate'],
                'location':dict1['location'],
                'fee':dict1['fee']
            }
        return
        
        
        
            
        
         
            
