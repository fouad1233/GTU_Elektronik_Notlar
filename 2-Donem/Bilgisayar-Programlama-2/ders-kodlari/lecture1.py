#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 22:14:07 2022

@author: fuad
"""
my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"

import random
def problem1(x):
    """
    Write a function that takes an integer nas an input
    and returns a one dimensional list with random integer entriesin [0:1000].
    You can use randomlibrary.
    ●Function parameter names do not matter,
    but the function should expect 1 parameter.
    ●Function won’t be tested for exceptional cases.
    ●input  :○n ∈ℤand n∈[1:104]
    ●output : x = { x : x is a list and x[i] ∈[0:1000]}
    >>> rl = problem1(3)
    """
    number_list = []
    for i in range(x):
        number_list.append(random.randint(0, 1000))
    return number_list


#one dimension peack find
def findpeack(a):
    
    finded = False
    while finded == False:
        lengh = len(a) - 1
        
        
        
        if a[lengh//2 + 1 ] > a[lengh//2]:
            a = a[lengh//2   ::]
        elif a[lengh//2 -1 ] > a[lengh//2]:
            a = a[0:lengh//2 :]
        
        else :
            return a[lengh//2 ]
        

#Grid ascene algorithm





if __name__ == "__main__":
    for i in  range(2,100):
        
        a = problem1(i)
        print(findpeack(a))
    print("Test")
    
    