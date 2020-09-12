# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:40:32 2020

@author: Dell
"""

x=1042000
while(x!=702648265):
    
    number =x
    orignal=number
    newn=0
    while(number >0):
        temp=number%10
        newn+=(temp**3)
        number=number//10
        
        
    if(newn==orignal):
      print(newn)
      break
    x+=1
    
    