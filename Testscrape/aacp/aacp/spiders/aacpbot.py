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
    #allowed_domains = ['www.aacp.org.uk']
    start_urls = ['https://www.aacp.org.uk/search?loc=Peterborough&distance=5']
           
    def parse(self, response):
        url1 = "https://www.aacp.org.uk/search?loc=Peterborough&distance="
        l1 = [5,10,25,50]
        for i in l1:
            url = url1 + str(i)
            yield scrapy.Request(url,callback=self.parse1)
    
    def parse1(self,response):    
        l2 = response.xpath("//script/text()").extract()
        l2 = l2[0]
        l2 = l2.replace("\r\n","")
        #l1 = l1.replace(" ","")
        l2 = l2.replace("$(document).ready","")
        l2 = l2.replace("function()","")
        l2 = l2.replace("Main.Layout.init();","")
        l2 = l2.replace("Main.Search.init","")
        
        l2 = l2.split(',')
        """
        for i in l2:
            #print('#################################################################')
            print(i)
            if(i.find('"updated_at"')!=-1):
                l2.remove(i)
            if(i.find('"created_at"')!=-1):
                l2.remove(i)
            if(i.find('"id"')!=-1):
                l2.remove(i)
            if(i.find('"remember_token"')!=-1):
                l2.remove(i)
            if(i.find('"flagged"')!=-1):
                l2.remove(i)
            if(i.find('""archived"')!=-1):
                l2.remove(i)
            if(i.find('"pivot"')!=-1):
                l2.remove(i)
            if(i.find('"activityinterest_id"')!=-1):
                l2.remove(i)
            if(i.find('"CSPmemberno"')!=-1):
                l2.remove(i)
            if(i.find('"HCPCmemberno"')!=-1):
                l2.remove(i)
            if(i.find('"emulation_key"')!=-1):
                l2.remove(i)
            if(i.find('"initialCpd"')!=-1):
                l2.remove(i)
            if(i.find('"username"')!=-1):
                l2.remove(i)
            
        """       
        name = []
        address = []
        town = []
        index1 = []
        country = []
        postcode = []
        phone = []
        email = []
        #for i in range(len(l2)):
            #print(str(i)+" #### "+l2[i])
        for i in range(len(l2)):
            if(l2[i].find("title")!=-1):
                str2 = l2[i][l2[i].find("title")+8:len(l2[i])-1]
                if(l2[i+1].find("firstname")!=-1):
                    str1 = (l2[i+1][l2[i+1].find("firstname")+12:len(l2[i+1])-1])
                    if(l2[i+2].find("surname")!=-1):  
                        str3 = l2[i+2][l2[i+2].find("surname")+10:len(l2[i+2])-1]
                        index1.append(i)
                        str4 = str2+" "+str1+" "+str3
                        name.append(str4)
        
        for i in range(len(index1)):
            if(i==0):
                for j in range(0,index1[i]):
                    if(l2[j].find("address1")!=-1):
                        str2 = l2[j][l2[j].find("address1")+11:len(l2[j])-1]
                    if(l2[j].find("address2")!=-1):
                        str1 = l2[j][l2[j].find("address2")+11:len(l2[j])-1]
                    if(l2[j].find("address3")!=-1):
                        str3 = l2[j][l2[j].find("address3")+11:len(l2[j])-1]
                    if(l2[j].find("town")!=-1):
                        str5 = l2[j]
                        str5 = str5.replace('"',"")
                        str5 = str5.replace("town","")
                        str5 = str5.replace(":","")
                    if(l2[j].find("county")!=-1):
                        str6 = l2[j][l2[j].find("county")+9:len(l2[j])-1]
                    if(l2[j].find("postcode")!=-1):
                        str7 = l2[j][l2[j].find("postcode")+11:len(l2[j])-1]
                    if(l2[j].find("phone")!=-1):
                        str8 = l2[j][l2[j].find("phone")+8:len(l2[j])-1]
                    if(l2[j].find("email")!=-1):
                        str9 = l2[j][l2[j].find("email")+8:len(l2[j])-1]
                str4 = str2+", "+str1+", "+str3
                address.append(str4)
                town.append(str5)
                country.append(str6)
                postcode.append(str7)
                phone.append(str8)
                email.append(str9)
            else:
                for j in range(index1[i-1],index1[i]):
                    #print(index1[i-1]," ",index1[i])
                    if(l2[j].find("address1")!=-1):
                        str2 = l2[j][l2[j].find("address1")+11:len(l2[j])-1]
                    if(l2[j].find("address2")!=-1):
                        str1 = l2[j][l2[j].find("address2")+11:len(l2[j])-1]
                    if(l2[j].find("address3")!=-1):
                        str3 = l2[j][l2[j].find("address3")+11:len(l2[j])-1]
                    if(l2[j].find("town")!=-1):
                        str5 = l2[j]
                        #print(str5)
                        str5 = str5.replace('"',"")
                        str5 = str5.replace("town","")
                        str5 = str5.replace(":","")
                    if(l2[j].find("county")!=-1):
                        str6 = l2[j][l2[j].find("county")+9:len(l2[j])-1]
                    if(l2[j].find("postcode")!=-1):
                        str7 = l2[j][l2[j].find("postcode")+11:len(l2[j])-1]
                    if(l2[j].find("phone")!=-1):
                        str8 = l2[j][l2[j].find("phone")+8:len(l2[j])-1]
                    if(l2[j].find("email")!=-1):
                        str9 = l2[j][l2[j].find("email")+8:len(l2[j])-1]
                str4 = str2+", "+str1+", "+str3
                address.append(str4)
                town.append(str5)
                country.append(str6)
                postcode.append(str7)
                phone.append(str8)
                email.append(str9)
        speciality = []
        for i in range(len(index1)):
            str1 = ""
            if(i<len(index1)-1):
                for j in range(index1[i],index1[i+1]):
                    if(l2[j].find('"name"')!=-1):
                        str2 = l2[j][l2[j].find("name")+7:len(l2[j])-1]
                        str1 = str1+str2+","
                speciality.append(str1)
            else:
                for j in range(index1[i],len(l2)):
                    if(l2[j].find('"name"')!=-1):
                        str2 = l2[j][l2[j].find("name")+7:len(l2[j])-1]
                        str1 = str1+str2+","
                speciality.append(str1)
        for i in range(len(name)):
            yield{
                'name':name[i],
                'address':address[i],
                'town':town[i],
                'country':country[i],
                'postcode':postcode[i],
                'phone':phone[i],
                'email':email[i],
                'speciality':speciality[i],
                }
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        