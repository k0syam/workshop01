# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:09:21 2021

@author: pi_na
"""

INF = 20000000

n = int(input())
a = list(map(int,input().split()))

#最小値の線形探索
v_min = INF
for i in range(n):
    v_min = min(v_min, a[i])

print(v_min)