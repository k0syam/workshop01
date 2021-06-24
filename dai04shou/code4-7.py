# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:18:51 2021

@author: pi_na
"""

f=[0]*50
f[0]=0
f[1]=1

for i in range(2,50):
    f[i] = f[i-1] + f[i-2]
    print(i,f[i])
