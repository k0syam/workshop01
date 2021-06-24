# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 21:27:02 2021

@author: pi_na
"""


n,w=map(int,input().split())

a=list(map(int,input().split()))

#globalで定義したaが呼び出される（リストの場合）

def func(i,w):
    #base case
    if i == 0:
        if w == 0:
            return True
        else:
            return False
        
    #a[i-1]を選ばない場合
    if func(i-1,w):
        return True
    #同時に呼び出されないように分けて記述
    #if func(i-1,w) or func(i-1,w-a[i-1])だと計算時間伸びる？
    #a[i-1]を選ぶ場合
    if func(i-1,w-a[i-1]):
        return True
    
    #どちらもFalseの場合
    return False



if func(n,w):
    print('Yes')
else:
    print('No')