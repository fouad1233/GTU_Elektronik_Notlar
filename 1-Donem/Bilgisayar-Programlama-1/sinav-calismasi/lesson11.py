#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 17:00:38 2022

@author: fuad
"""

import matplotlib.pyplot as plt
import time
#import math

def fib(n):
    '''
    

    Parameters
    ----------
    n : integer

    Returns the n th fibonacci number
    -------
    TYPE
        Function.

    '''
    global numFibCalls
    numFibCalls += 1
    if n==1:
        return 1
    if n== 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
upperbound = 30
a = []
a1 = []
for i in range(1,upperbound) :
    numFibCalls = 0
    t0 = time.time()
    fib(i)
    t1 = time.time() - t0
    a.append(numFibCalls)
    a1.append(t1)
    
ae= []
for i in range(1,upperbound):
    ae.append(2**i/4)

plt.figure(1)

plt.semilogy(range(1,upperbound),a)
    
plt.semilogy(range(1,upperbound),ae)   
b = [10,20,30,40,50,60,70,80]
plt.semilogy(range(1,9),b)
    
    
    
    
    
    
    