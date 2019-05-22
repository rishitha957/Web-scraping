# -*- coding: utf-8 -*-
"""
Created on Wed May 22 10:16:02 2019

@author: rishi
"""

import webbrowser,sys,pyperclip,bs4,requests

#webbrowser.open("https://inventwithpython.com/")

if(len(sys.argv)>1):
    #get address from command line arguments
    address = ' '.join(sys.argv[1:])
else:
    #get address from the clipboard using pyperclip package
    address = pyperclip.paste()
    
print(address)

#webbrowser.open('https://www.google.com/maps/place/'+address)
res = requests.get('http://google.com/search?q='+address)
res.raise_for_status()
print(res)
soup = bs4.BeautifulSoup(res.text,'lxml')
linkEl = soup.select('.r a')

num = min(5,len(linkEl))

for i in range(num):
    webbrowser.open('http://google.com'+linkEl[i].get('href'))