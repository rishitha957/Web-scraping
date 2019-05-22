# -*- coding: utf-8 -*-
"""
Created on Wed May 22 09:52:31 2019

@author: rishi
"""

import requests,bs4

res = requests.get('https://en.wikipedia.org/wiki/Friends')
#type(res)
#print(res.text[:250])

soup = bs4.BeautifulSoup(res.text,'lxml')
#type(soup)
list = soup.select('p')
for i in list[:5]:
    print(i.getText())