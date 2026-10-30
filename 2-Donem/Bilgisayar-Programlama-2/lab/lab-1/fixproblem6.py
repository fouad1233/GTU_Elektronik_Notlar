#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 17:09:49 2022

@author: fuad
"""
import random
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
    while True :
        rownum = len(rl) - 1
        colnum = len(rl[0]) - 1
        
        #1
          #finding global column max
        if count > 0:
            tested_indices.append([i,j])
        count = 1
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

if __name__ == "__main__":
    
    for i in range(2,100):
        
        rl = problem2(i,i)
        print(rl)
        print(problem6(rl))
    # We run the print on the function since we will be returning the value
    # and print() function will print whatever is passed within its parentheses.
    import doctest
    doctest.testmod()