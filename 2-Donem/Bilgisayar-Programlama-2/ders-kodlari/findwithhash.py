#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 10 21:01:03 2022

@author: fuad
"""

import string , random , matplotlib.pyplot as plt , time

def stringmaker(n):
    string_letters =  string.digits + string.ascii_letters
    element = ''.join(random.choice(string_letters) for i in range(n ))
    return element
    
def hashing(l):
    value  = 0
    a = 10
    for i in range (len(l)):
        value += ord(l[i]) *(a**(len(l)-i-1))
    return value
def substractandadd(l,value,index):
    a = 10
    value -= ( ord(l[0]) * (a**(len(l) - 1)) )
    value = value * a
    value += ord(index)
    return value
def findinlist(word,d):
    w_hash = hashing(word)
    d_firsthash = hashing(d[0:len(word)])
    if w_hash == d_firsthash:
        if d[0 : len(word)] == word:
            return True, 0
    else :
        d_firsthash = substractandadd(d[0:len(word)],d_firsthash,d[len(word)])
        if w_hash == d_firsthash:
            if d[1 : len(word) + 1 ] == word:
                return True, 1
    for i in range(1,len(d) - len(word) ):
        
                
        d_firsthash = substractandadd(d[i : i +len(word)  ],d_firsthash,d[len(word) + i ])
    
        if w_hash == d_firsthash:
            if d[i + 1 : i +  len(word) + 1  ] == word:
                return True ,i + 1
    return False
d = "bgabb"
word = "ab"
print(findinlist(word,d))
# y = []
# lmine = []
# lpython = []
# l = [1,2,2,43,3]
# l.sort()
# tone = time.perf_counter()
# for i in range(10000000,100000000,10000000):
#     y.append(i)
#     text = stringmaker(i)
#     word = stringmaker(2)
#     t1 = time.perf_counter()
#     print(findinlist(word,text))
#     t2 = time.perf_counter()
#     print(word in text)
#     t3 = time.perf_counter()
#     lmine.append(t2-t1)
#     lpython.append(t3-t2)
    

# plt.plot( y,lmine, label = "My own find in string function")
# plt.plot( y,lpython, label = "Phyton buit in 'in' function ")
# plt.ylabel('time')
# # naming the y axis
# plt.xlabel('lengh of list')
# #title
# plt.title('graph of sort algorithms efficiency')
# # show a legend on the plot
# plt.legend()

# # function to show the plot
# plt.show()
# tt = time.perf_counter()
# t = tt - tone
# print("You plot the graph in ",t, "seconds")

    

        