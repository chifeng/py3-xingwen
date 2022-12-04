#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 08:40:13 2022

@author: chifeng
"""

import math
import numpy as np

s = math.pow(10,10)
print (s)

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print (a[2][3])

#str = input()
str = "xingwen"
if str ==  ("xingwen"):
    print (str)
else:
    print ("xiaozonghou")
    
a = 2
b = 2
c = 3
if a == 1:
    if b == 2:
        print ("YES")
    else:
        print (c)

aa = 1
aa -= 2
aa = aa + 2
print (aa)

print (250**250)
a = 2
b = 5
c = 3

if a == b:
    print ("a is equal b")
elif a != b:
    print ("I don't know")
    

for i in range(1,500000):
    print (i)
    print ("xingwen")

#当不等于100的到时候，才循环
#str = '100'
while str != '100':
    print ("QUIT")
    str = input()
    
    
    
    