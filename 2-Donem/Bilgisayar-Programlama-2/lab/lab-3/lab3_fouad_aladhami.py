#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:41:57 2022

@author: fuad
"""

my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"

import random , numpy as np
def problem1(z1,z2,st):
    st = st.lower()
    if st == 'add' :
        return z1 + z2
    elif st == 'sub':
        return z1 - z2 
    elif st == 'mul':
        return z1 * z2
    elif st == 'div':
        return z1 / z2

def problem2(z , st):
    try :
        st = st.lower()
        if st == "abs":
            return np.abs(z)
        elif st == "ang":
            return np.angle(z)
        elif st == "pol":
            return (np.abs(z), np.angle(z) )
        elif st == "con":
            return np.conj(z)
    except :
        return None
def problem3(row,coulumn,emin,emax): 
    li = np.empty((0, coulumn))
    onecol = np.empty((0, coulumn))
    for i in range(row):
        for j in range(coulumn):
            onecol = np.append(onecol,(random.uniform(emin,emax) +random.uniform(emin,emax)*1j ))
            
        li = np.append(li,[onecol],axis = 0)
        onecol = np.empty((0, coulumn))
    return li
def problem4(n , emin , emax):
    vector = np.array([])
    for i in range(n):
        vector = np.append(vector,(random.uniform(emin,emax) +random.uniform(emin,emax)*1j ) )
    return vector
def problem5(mat , alpha):
    
    
    diagonal2d = np.diag(np.diag(mat))
    np.fill_diagonal(mat, alpha)
    mat = mat + diagonal2d

def problem6(a , b ):
    try : 
        return np.linalg.solve(a, b)
    except:
        return None
def problem7(a):
    try :
        x = np.linalg.inv(a) 
        return x
    except:
        return None
def problem8(a,b):
    try : 
        anintersi = np.linalg.inv(a)  == b
        bnintersi = a == np.linalg.inv(b)
        if anintersi.all() == True  :
            return True
        elif bnintersi.all() == True  :
            return True
        else :
            return False
    except : 
        return None

def problem9(a,b):
    try :
        return np.dot(a,b)
    except :
        return None
def problem10(a,st):
    try:
        st = st.lower()
        if st == 'det':
            return np.linalg.det(a)
        elif st == 'rank':
            return np.linalg.matrix_rank(a)
        elif st == 'eig':
            return np.linalg.eigvals(a)
        elif st == 'eigvec':
            return  np.linalg.eig(a)
        elif st == 'svd':
            return np.linalg.svd(a)
        else:
            return None
    except :
        return None
    