# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:15:38 2021

@author: pi_na
"""

def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    
    return fibo(n-1)+fibo(n-2)


for i in range(10):
    print(fibo(i))