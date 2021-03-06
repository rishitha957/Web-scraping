# -*- coding: utf-8 -*-
"""
Created on Wed May 22 11:38:15 2019

@author: rishi
"""

import requests,os,bs4

url = 'http://xkcd.com'

os.makedirs('xkcd',exist_ok=True)

while not url.endswith('#'):
    #download the webpage
    print('Downloading the webpage %s.....' %url)
    res = requests.get(url)
    res.raise_for_status()
    
    soup = bs4.BeautifulSoup(res.text,'lxml')
    
    #finding the url of the comic image
    
    comicElem = soup.select('#comic img')
    if(comicElem==[]):
        print('Could not find comic image')
    else:
        try:
            comicUrl = 'http:'+comicElem[0].get('src')
            #download image
            print('Downloading image %s....' %(comicUrl))
            res = requests.get(comicUrl)
            res.raise_for_status()
        except requests.exceptions.MissingSchema:
            prevLink = soup.select('a[rel="prev"]')[0]
            url = 'http://xkdc.com'+prevLink.get('href')
            continue
        #saving the image to ./xkcd
        imageFile = open(os.path.join('xkcd',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(5):
            imageFile.write(chunk)
        imageFile.close()
        
    #get the Prev button's url 
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com'+prevLink.get('href')

print("Done")
    
    
    
    
    
    
    
    
    