# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:09:35 2021

@author: pi_na
"""
import sys
#print(sys.getrecursionlimit()) 3000 環境によって異なる
sys.setrecursionlimit(10000)

#再帰呼び出しが止まらないケース
#pythonでは再帰呼び出し上限にひっかかるとエラー

def func(N):
    if N==0:
        return 0
    elif N>1000:
        return 0
    return N + func(N+1)

print(func(5))