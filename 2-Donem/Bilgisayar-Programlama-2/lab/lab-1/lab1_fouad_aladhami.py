#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 17:45:13 2022

@author: fuad
"""

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import random

my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"


#Problem 1 –Generate an array of random numbers [1pts]
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
#Problem 2 –Generate a matrix of random numbers [1pts]
def problem2(row,column):
    """
    Parameters
    ----------
    row : integer
    column : integer

    Returns 
    -------
    a list of lists with random integer entries in [0:1000]

    """
    number_list = []
    matrix = []
    for i in range(row):
        for j in range(column):
            number_list.append(random.randint(0, 1000))
        matrix.append(number_list)
        number_list = []
    return matrix

#Problem 3 –Straightforward 1D peak finder [3pts]
def problem3(rl, n = None ):
    """
    
    ●First parameter should consistsof a list with random entries, second parameter determines the starting index.
    ●Default value of the second parameter should be half of the length of the input list.
    ●Be careful about the order of the steps!Outputs will be evaluated also considering the steps of the algorithm.
    >>> rl= [250, 853, 376, 897, 704, 468, 281, 937, 396, 390]
    >>> valloc,loclist=problem3(rl)
    >>> print(valloc)
    (897, 3)
    >>> print(loclist)
    [5, 4, 3]
    >>> rl= [921, 343, 634, 507, 937, 613, 263, 866, 49, 780]
    >>> valloc,loclist=problem3(rl,1)
    >>> print(valloc)
    (634, 2)
    >>> print(loclist)
    [1, 2]
    >>> rl=[0,1,2,3,4,5,6,7,8,9]
    >>> valloc,loclist=problem3(rl,0)
    >>> print(valloc)
    (9, 9)
    >>> print(loclist)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    
    Parameters
    ----------
    rl : list 
    n : integer 'Starting index'

    Returns
    -------
    the peak value andlocation as a tupleand returns the indices of the tested elements.

    """
    if n == None:
        n = round(len(rl)/2)
    if n >= len(rl):
        return IndexError
        
    peak = 0
    peak_index = 0
    tested_indices = []
    finded = False
    while finded == False:
        if n < len(rl) -1 and n > 0:
            if rl[n] >= rl[n+1] and rl[n] >= rl[n-1]:
                finded = True
                tested_indices.append(n)
                peak_index = n 
                peak = rl[n]
                return ( (peak, peak_index) , tested_indices  )
            elif rl[n] >= rl[n+1] or n ==len(rl)-1:
                tested_indices.append(n)
                n=n-1
            else :
                tested_indices.append(n)
                n=n+1
        elif n < len(rl) -1 and n == 0:
            if rl[n] >= rl[n+1] :
                finded = True
                tested_indices.append(n)
                peak_index = n 
                peak = rl[n]
                return ( (peak, peak_index) , tested_indices  )
            
            else :
                tested_indices.append(n)
                n=n+1
        elif n == len(rl) -1 and n > 0:
            if  rl[n] >= rl[n-1]:
                finded = True
                tested_indices.append(n)
                peak_index = n 
                peak = rl[n]
                return ( (peak, peak_index) , tested_indices  )
            
            else :
                tested_indices.append(n)
                n=n-1 
        elif n == len(rl) -1 and n == 0:
            
                finded = True
                tested_indices.append(n)
                peak_index = n 
                peak = rl[n]
                return ( (peak, peak_index) , tested_indices  )
#Problem 4 –Divide and conquer based 1D peak finder [5pts]
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
    if n == None:
        n = round(len(rl)/2)
    if n >= len(rl):
        return IndexError
    
    peak = 0
    peak_index = ()
    tested_indices = []
    distance_list = []
    direction_list = []
    while True:
        tested_indices.append(n)

        if len(tested_indices) >= 2:
            distance_list = []
            for i in range(len(tested_indices) ):
                distance_list.append(tested_indices[-1] -tested_indices[i] )
                
            
        if n < len(rl) -1 and n > 0 :
            if rl[n] >= rl[n+1] and rl[n] >= rl[n-1]:
                peak_index = n 
                peak = rl[n]
                return ( (peak, peak_index) , tested_indices )
                
            elif rl[n]<rl[n-1] and n != 0:
                direction_list.append('left')
                
                if len(direction_list) >= 2:
                    left_near = []
                    for i in range(len(distance_list)):
                        if distance_list[i] > 0 :
                            left_near.append(distance_list[i])
                    if len(left_near) >= 1:
                        n2 = min(left_near)
                    if direction_list[-1] != direction_list[-2]:
                        if len(left_near) >= 1:
                            n = round( (tested_indices[-1] + n2 + tested_indices[-1]) / 2)
                        else:
                            n = round( (tested_indices[-1] + tested_indices[-2]) / 2)
                    else : 
                        
                        n=round((n-1)/2)
                else :
                    n=round((n-1)/2)
            elif  rl[n]<rl[n+1] and n !=len(rl)-1:
                direction_list.append('right')
                
                if len(direction_list) >= 2:
                    right_near = []
                    for i in range(len(distance_list)):
                        if distance_list[i] < 0 :
                            right_near.append(distance_list[i])
                    if len(right_near) >= 1:
                        n2 = max(right_near)
                        
                    if direction_list[-1] != direction_list[-2]:
                        if len(right_near) >= 1:
                            n = round( (tested_indices[-1] - n2 +tested_indices[-1]) / 2)
                        else : 
                            n=round( (n + len(rl) ) / 2)
                    else : 
                        
                        n=round( (n + len(rl) ) / 2)
                else :
                    n=round( (n + len(rl) ) / 2)
                    
            else:
                return 'Peak not founded'
            
              
        elif n == len(rl) - 1 and  rl[n] >= rl[n-1]:
             peak_index = n 
             peak = rl[n]
             return ( (peak, peak_index) , tested_indices )
        elif n == len(rl) - 1  and rl[n] < rl[n -1 ]:
            direction_list.append('left')
            
            if len(direction_list) >= 2:
                left_near = []
                for i in range(len(distance_list)):
                    if distance_list[i] > 0 :
                        left_near.append(distance_list[i])
                if len(left_near) >= 1:
                    n2 = min(left_near)
                if direction_list[-1] != direction_list[-2]:
                    if len(left_near) >= 1:
                        n = round( (tested_indices[-1] + n2 + tested_indices[-1]) / 2)
                    else:
                        n = round( (tested_indices[-1] + tested_indices[-2]) / 2)
                else : 
                    
                    n=round((n-1)/2)
            else :
                n=round((n-1)/2)
        elif n == 0 and  rl[n] < rl[n+1]:
             direction_list.append('right')
             
             if len(direction_list) >= 2:
                 right_near = []
                 for i in range(len(distance_list)):
                     if distance_list[i] < 0 :
                         right_near.append(distance_list[i])
                 if len(right_near) >= 1:
                     n2 = max(right_near)
                     
                 if direction_list[-1] != direction_list[-2]:
                     if len(right_near) >= 1:
                         n = round( (tested_indices[-1] - n2 +tested_indices[-1]) / 2)
                     else : 
                         n=round( (n + len(rl) ) / 2)
                 else : 
                     
                     n=round( (n + len(rl) ) / 2)
             else :
                 n=round( (n + len(rl) ) / 2)
        elif n== 0 and rl[n]>=rl[n+1]:
             peak_index = n 
             peak = rl[n]
             return ( (peak, peak_index) , tested_indices )
        elif len(rl) ==  1 :
            peak_index = n 
            peak = rl[n]
            return ( (peak, peak_index) , tested_indices )
        else:
             return 'Peak not founded'
         

#Problem 5 –Straightforward 2D peak finder [4pts]
def problem5(rl,i = None,j = None): 
    """
    >>> rl= [[485, 972, 829], [522, 32, 696], [651, 965, 476], [389, 724, 185]]
    >>> valloc,loclist=problem5(rl)
    >>> print(valloc)
    (972, [0, 1])
    >>> print(loclist)
    [[2, 2], [1, 2], [0, 2], [0, 1]]
    >>> rl= [[861, 93, 242, 477, 324], [936, 198, 177, 914, 944], [315, 211, 479, 717, 348], [544, 712, 667, 967, 119], [816, 920, 155, 419, 57]]
    >>> valloc,loclist=problem5(rl,0,0)
    >>> print(valloc)
    (936, [1, 0])
    >>> print(loclist)
    [[0, 0], [1, 0]]
    >>> valloc,loclist=problem5(rl,4,4)
    >>> print(valloc)
    (944, [1, 4])
    >>> print(loclist)
    [[4, 4], [3, 4], [2, 4], [1, 4]]

    Parameters
    ----------
    rl : Random list
    i : Start index of row
    j : Start index of column

    Returns
    -------
    peak : TYPE
        DESCRIPTION.
    peak_index : Tuple
    tested_indices : List of tuples

    """
    if i == None :
        i = round(len(rl)/2)
    if j == None :
        j = round(len(rl[0])/2)
    rownum = len(rl) - 1
    colnum = len(rl[0]) - 1
    peak = 0
    peak_index = ()
    tested_indices = []
    finded = False
    while finded == False:
        tested_indices.append([i,j])
        #1
        if i>0 and j>0 and i< rownum and j < colnum: 
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif  rl[i-1][j]>= rl[i][j]and i!=0:
                i = i - 1
            
            elif rl[i][j-1] >= rl[i][j] and j!=0:
                j=j-1
                
            elif rl[i+1][j]>= rl[i][j]and i!=len(rl)-1:
                i = i+1
            
            elif rl[i][j+1]>=rl[i][j] and j!=len(rl[0])-1:
                j=j+1
        #2
        elif i>0 and j>0 and i< rownum and j == colnum: 
            if rl[i][j] >= rl[i+1][j]  and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif  rl[i-1][j]>= rl[i][j]and i!=0:
                i = i - 1
                
            elif rl[i][j-1] >= rl[i][j] and j!=0:
                j=j-1
                
            elif rl[i+1][j]>= rl[i][j]and i!=len(rl)-1:
                i = i+1
              
        #3    
        elif i>0 and j>0 and i == rownum and j < colnum: 
            if  rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif  rl[i-1][j]>= rl[i][j]and i!=0:
                i = i - 1
            
            elif rl[i][j-1] >= rl[i][j] and j!=0:
                j=j-1
            
            elif rl[i][j+1]>=rl[i][j] and j!=len(rl[0])-1:
                j=j+1
        #4       
        elif i>0 and j>0 and i == rownum and j == colnum: 
            if  rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif  rl[i-1][j]>= rl[i][j]and i!=0:
                i = i - 1
            
            elif rl[i][j-1] >= rl[i][j] and j!=0:
                j=j-1
        #5
        elif i == 0 and j>0 and i < rownum and j < colnum: 
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1]  and rl[i][j] >= rl[i][j-1]:
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            
            elif rl[i][j-1] >= rl[i][j] and j!=0:
                j=j-1
                
            elif rl[i+1][j]>= rl[i][j]and i!=len(rl)-1:
                i = i+1
            
            elif rl[i][j+1]>=rl[i][j] and j!=len(rl[0])-1:
                j=j+1
        #6
        elif i > 0 and j == 0 and i < rownum and j < colnum: 
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] :
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif  rl[i-1][j]>= rl[i][j]and i!=0:
                i = i - 1
            
            elif rl[i+1][j]>= rl[i][j]and i!=len(rl)-1:
                i = i+1
            
            elif rl[i][j+1]>=rl[i][j] and j!=len(rl[0])-1:
                j=j+1    
        #7
        elif i == 0 and j == 0 and i < rownum and j < colnum:
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] :
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
               
            elif rl[i+1][j]>= rl[i][j]and i!=len(rl)-1:
                i = i+1
            
            elif rl[i][j+1]>=rl[i][j] and j!=len(rl[0])-1:
                j=j+1
        #8
        elif i > 0 and j == 0 and i == rownum and j < colnum:
            if  rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] :
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif  rl[i-1][j]>= rl[i][j]and i!=0:
                i = i - 1
            elif rl[i][j+1]>=rl[i][j] and j!=len(rl[0])-1:
                j=j+1
        #9
        elif i == 0 and j > 0 and i < rownum and j == colnum:
            if rl[i][j] >= rl[i+1][j]  and rl[i][j] >= rl[i][j-1]:
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1] >= rl[i][j] and j!=0:
                j=j-1
                
            elif rl[i+1][j]>= rl[i][j]and i!=len(rl)-1:
                i = i+1
        #10 for 1 element list like [[23]]
        elif i == 0 and j == 0 and i == rownum and j == colnum:
            finded = True
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )    
        #11 
        elif i == 0 and j == 0 and i == rownum and j < colnum:
            if  rl[i][j]>=rl[i][j+1] :
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j+1]>=rl[i][j] and j!=len(rl[0])-1:
                j=j+1
        #12
        elif i == 0 and j > 0 and i == rownum and j == colnum:
            if  rl[i][j] >= rl[i][j-1]:
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            
            elif rl[i][j-1] >= rl[i][j] and j!=0:
                j=j-1
        #13
        elif i == 0 and j == 0 and i < rownum and j == colnum:
            if rl[i][j] >= rl[i+1][j] :
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
                
            elif rl[i+1][j]>= rl[i][j]and i!=len(rl)-1:
                i = i+1
        #14
        elif i > 0 and j == 0 and i == rownum and j == colnum:
            if rl[i][j]>=rl[i-1][j] :
                finded = True
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif  rl[i-1][j]>= rl[i][j]and i!=0:
                i = i - 1
        else:
            finded = True
            return 'Peak not founded'

def copylist(board):
    c = 0
    yeniliste = []
    for i in range(len(board)):
        yeniliste.append([])
        
        a = len(board[0])
        for i in range(a):
            yeniliste[c].append(board[c][i])
        c +=1
    return yeniliste

def problem6(rl,i = None,j = None):
    
    """
    >>> rl= [[718, 239, 177, 770], [777, 663, 630, 300], [595, 726, 6, 73], [253, 105, 879, 863], [189, 862, 277, 682]]
    >>> valloc,loclist=problem6(rl)
    >>> print(valloc)
    (879, [3, 2])
    >>> print(loclist)
    [[2, 2], [3, 2]]
    
    >>> rl=[[399, 922, 327, 971], [767, 854, 256, 106], [339, 25, 74, 183], [613, 746, 126, 114], [558, 368, 880, 822]]
    >>> valloc,loclist=problem6(rl,0,0)
    >>> print(valloc)
    (880, [4, 2])
    >>> print(loclist)
    [[0, 0], [1, 0], [1, 2], [4, 2]]
    
    Parameters
    ----------
    rl : Random list
    i : İnteger
    j : İnteger

    Returns
    -------
    TYPE
        DESCRIPTION.

    """
    if i == None :
        i = round(len(rl)/2)
    if j == None :
        j = round(len(rl[0])/2)
    rownum = len(rl) - 1
    colnum = len(rl[0]) - 1
    peak = 0
    peak_index = ()
    tested_indices = []
    tested_indices.append([i,j])

    if i>0 and j>0 and i< rownum and j < colnum: 
        if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
            
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i>0 and j>0 and i< rownum and j == colnum: 
        if rl[i][j] >= rl[i+1][j]  and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i>0 and j>0 and i == rownum and j < colnum: 
        if  rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i>0 and j>0 and i == rownum and j == colnum: 
        if  rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i == 0 and j>0 and i < rownum and j < colnum: 
        if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1]  and rl[i][j] >= rl[i][j-1]:
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i > 0 and j == 0 and i < rownum and j < colnum: 
        if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] :
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i == 0 and j == 0 and i < rownum and j < colnum:
        if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] :
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i > 0 and j == 0 and i == rownum and j < colnum:
        if  rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] :
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i == 0 and j > 0 and i < rownum and j == colnum:
        if rl[i][j] >= rl[i+1][j]  and rl[i][j] >= rl[i][j-1]:
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i == 0 and j == 0 and i == rownum and j == colnum:
        
        peak_index = [i,j]
        peak = rl[i][j]
        return ( (peak, peak_index) , tested_indices )  
    elif i == 0 and j == 0 and i == rownum and j < colnum:
        if  rl[i][j]>=rl[i][j+1] :
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i == 0 and j > 0 and i == rownum and j == colnum:
        if  rl[i][j] >= rl[i][j-1]:
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i == 0 and j == 0 and i < rownum and j == colnum:
        if rl[i][j] >= rl[i+1][j] :
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    elif i > 0 and j == 0 and i == rownum and j == colnum:
        if rl[i][j]>=rl[i-1][j] :
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )
    else:
        pass
    direction_list = []
    distance_list = []
    count = 0
    same = 0
    while True :
        rownum = len(rl) - 1
        colnum = len(rl[0]) - 1
        
        #1
          #finding global column max
        if count > 0:
            tested_indices.append([i,j])
        if count > 1000000:
            return
        if len(tested_indices) > 2:
            if tested_indices[-1] == tested_indices[-2]:
                same += 1
        if same > 10 :
            return
        count += 1
        colelementlist = []
        for x in range(len(rl)):
            colelementlist.append(rl[x][j])#in one column
        colmax = colelementlist[0]
        #imax = 0
        for y in range(1,len(colelementlist)):
            if colelementlist[y]> colmax:
                colmax = colelementlist[y]
                imax = y
                i = imax   
        tested_indices.append([i,j])
        
        #checking peak
        #print(i,j)
        #print(rl)
        if i>0 and j>0 and i< rownum and j < colnum: 
            #print(i,j)
            #print(rl)
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
            
                
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
                
                
        elif i>0 and j>0 and i< rownum and j == colnum: 
            if rl[i][j] >= rl[i+1][j]  and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
                
            
        elif i>0 and j>0 and i == rownum and j < colnum: 
            if  rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
                
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
        elif i>0 and j>0 and i == rownum and j == colnum: 
            if  rl[i][j]>=rl[i-1][j] and rl[i][j] >= rl[i][j-1]:
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
                
            
        elif i == 0 and j>0 and i < rownum and j < colnum: 
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1]  and rl[i][j] >= rl[i][j-1]:
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
                
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
        elif i > 0 and j == 0 and i < rownum and j < colnum: 
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] :
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
        elif i == 0 and j == 0 and i < rownum and j < colnum:
            if rl[i][j] >= rl[i+1][j] and rl[i][j]>=rl[i][j+1] :
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
        elif i > 0 and j == 0 and i == rownum and j < colnum:
            if  rl[i][j]>=rl[i][j+1] and rl[i][j]>=rl[i-1][j] :
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
        elif i == 0 and j > 0 and i < rownum and j == colnum:
            if rl[i][j] >= rl[i+1][j]  and rl[i][j] >= rl[i][j-1]:
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
                
            
        elif i == 0 and j == 0 and i == rownum and j == colnum:
            
            peak_index = [i,j]
            peak = rl[i][j]
            return ( (peak, peak_index) , tested_indices )  
        elif i == 0 and j == 0 and i == rownum and j < colnum:
            if  rl[i][j]>=rl[i][j+1] :
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
        elif i == 0 and j > 0 and i == rownum and j == colnum:
            if  rl[i][j] >= rl[i][j-1]:
                
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
                
            elif rl[i][j+1]>rl[i][j] and j!=len(rl[0])-1:
                j=round( (j + len(rl) ) / 2)
                
                
        elif i == 0 and j == 0 and i < rownum and j == colnum:
            if rl[i][j] >= rl[i+1][j] :
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
                
        elif i > 0 and j == 0 and i == rownum and j == colnum:
            if rl[i][j]>=rl[i-1][j] :
                
                peak_index = [i,j]
                peak = rl[i][j]
                return ( (peak, peak_index) , tested_indices )
            elif rl[i][j-1]>rl[i][j] and j != 0:
                j=round((j-1)/2)
                
        else:
            return ('Peak not founded')
problem6([[926, 854, 999, 543], [899, 522, 814, 307], [53, 468, 154, 410]])
if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
    # for i in range(2,100):
    #     for j in range(2,100):
    #         rl = problem2(i,j)
    #         print(rl)
    #         print(problem6(rl))
    # We run the print on the function since we will be returning the value
    # and print() function will print whatever is passed within its parentheses.
    import doctest
    doctest.testmod()
    

