# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:55:35 2020

@author: hp 3006tx
"""


for i in range(2,201):
    temp=0    
    for j in range(2,i):
        
        if i%j==0:
           temp=1
           break
    if temp==0:     
         print(i) 
      