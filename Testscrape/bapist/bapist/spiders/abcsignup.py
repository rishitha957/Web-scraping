# -*- coding: utf-8 -*-
import scrapy
import re

class AbcsignupSpider(scrapy.Spider):
    name = 'abcsignup'
    #allowed_domains = ['abcsignup.com']
    start_urls = ['http://abcsignup.com/']

    def parse(self, response):
        url1 = "https://reg.abcsignup.com/view/cal2a.aspx?ek=&ref=&aa=&sid1=&sid2=&as=22&wp=259&tz=&ms=5&nav=&cc=&cat1=&cat2=&cat3=&aid=BHCP&rf=#"
        for i in range(1,13):
            url = url1[:87]+str(i)+url1[88:]
            yield scrapy.Request(url,callback=self.parse1)

    def parse1(self,response):
        link = response.xpath("//li[@class='cal_list_item']/a/@href").extract()
        for i in link:
            yield scrapy.Request(i,callback= self.parse2)
            
    def parse2(self,response):
        dict1 = {}
        list1 = []
        name = response.css("#event_page_header_logo~ .module_style .header_style div::text").extract()
        name.append(response.css("span strong span::text").extract())
        #set1 = response.xpath("//div[@class='content_style']/div[@style='padding:10px;']/p/span[@style='font-size: 12pt; font-family: Helvetica;']/text()").extract()
        dict1['name']=name
        temp2=response.css("p:nth-child(7) span::text").extract()
        if(len(temp2)==0):
            temp2=response.css("#event_page_header_logo~ .module_style .content_style div::text").extract()
        dict1['event_date'] = temp2
        dict1['event_time']=response.css("#event_page_header_logo~ .module_style p:nth-child(5) span::text").extract()
        dict1['status']=response.css(".left_pane p:nth-child(1) > span::text").extract()
        fee1 = response.css(".right_pane .module_style:nth-child(1) span::text").extract()
        fee1 = fee1[0]
        re1 = r'\$([0-9.]*[0-9]*)'
        fee = re.search(re1,fee1)
        dict1['fee']=fee.group()
        temp = response.css(".right_pane .module_style:nth-child(3) span::text").extract()
        if(len(temp)==0):
            temp = response.css(".right_pane br+ .module_style p span::text()").extract()
        dict1['ceu']=temp
        temp1=response.css(".module_style:nth-child(5) span::text").extract()
        if(len(temp1)==0):
            temp1 = response.css(".right_pane .module_style:nth-child(1) .content_style div::text").extract()
        dict1['location'] = temp1
        list1.append(dict1)
        for dict1 in list1:
            yield{
                'name' : dict1['name'],
                'event_date':dict1['event_date'],
                'event_time':dict1['event_time'],
                'status':dict1['status'],
                'fee':dict1['fee'],
                'ceu':dict1['ceu'],
                'location':dict1['location']
            }
        
        
        
        