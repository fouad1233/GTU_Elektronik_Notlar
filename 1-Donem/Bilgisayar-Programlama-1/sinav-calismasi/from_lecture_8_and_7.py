#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:57:28 2022

@author: fuad
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom 
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom) 
    def getNumer(self):
        return self.numer
    def getDenom(self):
        return self.denom
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() \
            + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew) 
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer()\
            - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom() 
        return fraction(numerNew, denomNew)
    def convert(self):
        return self.getNumer() / self.getDenom()
    
    
    
    
    
def avg(grades):    
    assert not len(grades) == 0, 'no grades data'
    return sum(grades)/len(grades)    

def isPal(x):
    assert type(x) == list 
    temp = x[:]
    
    temp.reverse()
    #print(x)
    if temp == x:
        return True
    else:
        return False

def silly(n):
    result = []
    for i in range(n):
            
            elem = input('Enter element: ')
            result.append(elem)
    #print(result)
    if isPal(result):
        print('Yes')
    else:
        print('No')
    
    

    
    
    
    
    