#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:07:29 2022

@author: fuad
"""
import time  , matplotlib.pyplot as plt
import lab2_fouad_aladhami_210102002808 as fouad

def problem2_kaan(slist):
    start = time.perf_counter_ns()
    for i in range(len(slist)):
        for j in range(i):
            if slist[i] < slist[j]:
                temp = slist[i]
                slist[i] = slist[j]
                slist[j] = temp
                break
    stop = time.perf_counter_ns()
    return stop - start

t1 = time.perf_counter()
y = []
x_f = []
x_k = []
for i in range(0,10**4,1000):
    y.append(i)
    rl = fouad.problem1(i)
    a = rl.copy()
    x_f.append(fouad.problem2(a)/10**9)
    a = rl.copy()
    x_k.append(problem2_kaan(a)/10**9)
plt.plot( y,x_k, label = "Insertion Sort by Kaan")
plt.plot( y,x_f, label = "Insertion Sort by Fouad")

plt.ylabel('time')
# naming the y axis
plt.xlabel('lengh of list')
#title
plt.title('graph of sort algorithms efficiency')
# show a legend on the plot
plt.legend()

# function to show the plot
plt.show()
t2 = time.perf_counter()
t = t2 - t1
print("You plot the graph in ",t, "seconds == ", t/60, "minute" )
