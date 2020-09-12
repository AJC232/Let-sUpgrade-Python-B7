# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:22:57 2020

@author: Dell
"""

for i in range(2,201):
    count = 0
    for j in range(2,i):
        if(i%j==0):
            count=1
            break
    
    if(count==0):
        print(i)
        
        
