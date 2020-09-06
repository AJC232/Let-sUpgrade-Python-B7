# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 19:34:05 2020

@author: hp 3006tx
"""
#num=1042000  
#while num<702648265:
num=1042000
while num!=702648265:
       
      dnum=num
      nnum=0
      while dnum>0:
          temp=dnum%10
          nnum+=(temp**3)
          dnum=dnum//10
          
          
      if(nnum==num):
          print('Armstrong Number is: ', nnum)
          break
      
      num+=1
      
     
        
        
      