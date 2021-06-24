# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:05:00 2021

@author: pi_na
"""

#再帰呼び出しテスト
def func(N):
    if N==0:
        return 0
    return N + func(N-1)

print(func(5))