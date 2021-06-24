# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 21:56:42 2021

@author: pi_na
"""

n, v = map(int,input().split())
a = list(map(int,input().split()))

#線形探索
exist = False

for i in range(n):
    if a[i] == v:
        exist = True

if exist:
    print('Yes')
else:
    print('No')

