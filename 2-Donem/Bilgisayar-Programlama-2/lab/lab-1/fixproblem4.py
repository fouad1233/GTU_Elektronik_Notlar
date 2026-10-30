#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  8 13:19:54 2022

@author: fuad
"""

import random

my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"


def problem1(x):
    
    number_list = []
    for i in range(x):
        number_list.append(random.randint(0, 1000))
    return number_list
class holder():
    
    id_counter = 0
    #players_and_points = {}
    #detailed_points = []
    def __init__(self,num):
        self.id = holder.id_counter
        holder.id_counter += 1
        self.num = num
    def get_num(self):
        return self.num
    def get_id(self):
        return self.id
    def reset(self):
        holder.id_counter = 0
    def __lt__(self, other ):
        if self.num < other.num :
            return True 
        else:
            return False 
    def __eq__(self, other):
        if self.num == other.num:
            return True
        else:
            return False
    def __le__(self, other):
        return self.num <= other.num
def problem4(rl, n = None):
    """
    >>> rl= [293, 170, 207, 323, 963, 445, 351, 921, 165, 759]
    >>> valloc,loclist=problem4(rl)
    >>> print(valloc)
    (963, 4)
    >>> print(loclist)
    [5, 2, 4]
    
    >>> rl=[0,1,2,3,4,5,6,7,8,9]
    >>> valloc,loclist=problem4(rl)
    >>> print(valloc)
    (9, 9)
    >>> print(loclist)
    [5, 8, 9]
    
    >>> rl=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    >>> valloc,loclist=problem4(rl)
    >>> print(valloc)
    (16, 16)
    >>> print(loclist)
    [8, 12, 14, 16]
    
    Parameters
    ----------
    rl : list
    n : integer 'the starting index'
    

    Returns
    -------
    None.

    """
    a = []
    for i in rl:
        a.append( holder(i) )
    if n == None:
        n = round(len(rl)/2)
    if n >= len(rl) or n< 0:
        return IndexError
    a[0].reset()
    peak = 0
    peak_index = ()
    tested_indices = []
    while True:
        if n < len(a) -1 and n > 0 :
            
            if a[n] >= a[n+1] and a[n] >= a[n-1]:
                tested_indices.append(a[n].get_id())
                peak_index = a[n].get_id() 
                peak = a[n].get_num()
                return ( (peak, peak_index) , tested_indices )
                
            elif a[n]<a[n-1] and n != 0:
                tested_indices.append(a[n].get_id())

                a = a[0:n]
                #print(rl,b,n )
                n=round((n-1)/2)
            elif  a[n]<a[n+1] and n !=len(a)-1:
                tested_indices.append(a[n].get_id())
                #d =  a[n].get_id() - len(rl)//2- 1
                
                a = a[n+1::]
                #print(rl,b,n )
                
                n=round((len(a)   )/2  )
                
    
            elif len(a) ==  1 :
                tested_indices.append(a[n].get_id())
                peak_index = a[n].get_id() 
                peak = a[n].get_num()
                return ( (peak, peak_index) , tested_indices )
            else:
                return 'Peak not founded1'
            
        elif n == len(a) - 1 and  a[n] < a[n-1]:
             tested_indices.append(a[n].get_id())
             a = a[0:n]
             #print(rl,b,n )
             n=round((n-1)/2) 
        elif n == len(a) - 1 and  a[n] >= a[n-1]:
             tested_indices.append(a[n].get_id())
             peak_index = a[n].get_id() 
             peak = a[n].get_num()
             return ( (peak, peak_index) , tested_indices )
        elif n== 0 and a[n] >= a[n + 1]:
             tested_indices.append(a[n].get_id())
             peak_index = a[n].get_id() 
             peak = a[n].get_num()
             return ( (peak, peak_index) , tested_indices )
        elif n== 0 and a[n] < a[n + 1]:
             tested_indices.append(a[n].get_id())
             #d =  a[n].get_id() - len(rl)//2- 1
             
             a = a[n+1::]
             #print(rl,b,n )
             
             n=round((len(a)   )/2  )
        # elif n > len(a)-1:
        #     n -= 1
        else:
             return 'Peak not founded'
# aşağıdaki kodları debug operasyonu için kullanabilirsiniz         
# rl=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# print(problem4(rl))
class inx_holder():

    inx_counter = 0
    def _init_(self,num):
        self.inx = inx_holder.inx_counter
        inx_holder.inx_counter += 1
        self.num = num

    def get_num(self):
        return self.num

    def get_inx(self):
        return self.inx

    def reset(self):
        inx_holder.inx_counter = 0

    def _lt_(self, other ):
        return self.num < other.num

    def _eq_(self, other):
        return self.num == other.num
        
    def _le_(self, other):
        return self.num <= other.num
    


rl = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
def problem4_erhan(rl,n=None):
    rl_holder=[]
    for i in rl:
        rl_holder.append(inx_holder(i))

    if n==None:
        n=round(len(rl)/2)
    tested=[]

    while True:
        tested.append(rl_holder[n].get_inx())
        if len(rl_holder)==1 or len(rl_holder)==1:
            return (rl_holder[n].get_num(),rl_holder[n].get_inx()),tested
        elif n==0:
            if rl_holder[n]>rl_holder[n+1]:
                return (rl_holder[n].get_num(),rl_holder[n].get_inx()),tested
            else:
                rl_holder=rl_holder[n+1:]
                n=round(len(rl_holder)/2)
        elif n==len(rl_holder)-1:
            if rl_holder[n]>rl_holder[n-1]:
                return (rl_holder[n].get_num(),rl_holder[n].get_inx()),tested
            else: 
                rl_holder=rl_holder[0:n]
                n=round(len(rl_holder)/2)
        else:
            if rl_holder[n]>=rl_holder[n+1] and rl_holder[n]>=rl_holder[n-1]:
                return (rl_holder[n].get_num(),rl_holder[n].get_inx()),tested
            elif rl_holder[n-1]>rl_holder[n]:

                rl_holder=rl_holder[0:n]
                n=round(len(rl_holder)/2)
            elif rl_holder[n+1]>rl_holder[n]:

                rl_holder=rl_holder[n+1:]
                n=round(len(rl_holder)/2)

    
if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

    # We run the print on the function since we will be returning the value
    # and print() function will print whatever is passed within its parentheses.
    import doctest
    doctest.testmod()
    #n i default için deneme kodu
    # no = []
    # for i in range(1,50):
    #     rl = problem1(i)
    #     print(rl)
    #     if problem4(rl)[0][0] == problem4_erhan(rl)[0][0]:
    #         print(i,True)
    #     else:
    #         no.append(rl)
    #         print(i,False)
    
        
    
    # n 6 için deneme kodu , 6 olarak seçilmemesinin herhangi bir nedeni yok
    #sadece dikkat edelmesi gerken husus  n in len(rl) - 1 den  küçük olması yoksa tanımladığım indexError döndürelecektir.
    # for i in range(7,1000):
    #     rl = problem1(i)
    #     print(rl)
    #     print(problem4(rl, 6))
    