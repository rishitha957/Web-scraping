# -*- coding: utf-8 -*-
"""
Created on Sat May 25 09:12:45 2019

@author: rishi
"""


li2 = []
li3 = [1,2,3,4]
li2.append(li3)
li4 = ['a','b','c','d']
li2.append(li4)

print(li2)
k = 0;
for i in range(len(li2)):
    while(k<len(li2[i])):
        print(li2[i][k])
        k = k+1
        
