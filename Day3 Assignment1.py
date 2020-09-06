# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:46:47 2020

@author: hp 3006tx
"""

alt = int(input('Enter Altitude: '))

if alt<=1000:
   print('Safe to Land')
elif alt<=5000:
   print('Bring down to 1000ft')
else:
   print('Go around and try after 10 minutes')