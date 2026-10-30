#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 12 07:29:09 2022

@author: fuad

"""
from lesson11 import fib
L = [1, -2, 3.4]
def applyToEach(L, f):
    for i in range(len(L)):
            L[i] = f(L[i])
def fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
applyToEach(L, abs)
applyToEach(L, int)
applyToEach(L, fact)
applyToEach(L, fib)

def applyFuns(L, x): 
    for f in L:
        print(f(x))

# for elt in map(abs, [1, -2, 3, -4]): 
#     print(elt)

# L1 = [1, 28, 36]
# L2 = [2, 57, 9]
# for elt in map(min, L1, L2): print(elt)


n = 'fouad aladhami      '

my_dict ={}
grades = {'Ana':'B', 'John':'A+', 'Daniel':'A', 'Katy':'A'}

#grades[list(grades.keys())[0]]

grades['Sylvan'] = 'A' #add



def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
           myDict[word] += 1 
        else:
           myDict[word] = 1
    return myDict

def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
    return (words, best)


def fib_efficient(n,d):
    if n in  d:
        return d[n]
    else:
        ans = fib_efficient(n-1,d)  +fib_efficient(n-2,d)
        d[n] = ans 
        return ans


d = {1:1, 2:1}
print(fib_efficient(6, d))



# L1 = [2,1,3]
# L2 = [4,5,6]
# L3 = L1 + L2
# L1.append(0)
# #L1.extend([0,6])

L = [2,1,3,6,3,2,7,0]
a = (1,3,1000)
b = (1,3,2000)









