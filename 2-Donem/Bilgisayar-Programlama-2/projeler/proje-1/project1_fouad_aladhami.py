#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 23 22:44:19 2022

@author: fuad
"""
my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"

import bstgtu as bst , avlgtu as avl , time

def reltime(t , tbase = "070000"):
    time_s = (int(t[0:2]) * 3600 +  int(t[2:4]) * 60 + int(t[4:6]) ) - (int(tbase[0:2]) * 3600 +  int(tbase[2:4]) * 60 + int(tbase[4:6]) )  
    return time_s

def read2tree(filename, TreeType, tbase='070000', tceil='220000'):
    fvalues = open(filename , "r")
    a = fvalues.read()
    values = a.strip().split('\n')
    fvalues.close()
    l = []
    for i in values:
        l.append(i.strip().split())
    if TreeType == 'BST':
        tree = bst.BST()
        for i in l:
            if int(i[0]) < int(tceil)  and int(i[0]) > int(tbase) :
                t = reltime(i[0] , tbase )
                tree.insert( t )
                tree.find(t).set_gtu(float(i[1]))
    elif TreeType == 'AVL':
        tree = avl.AVL()
        for i in l:
            if int(i[0]) < int(tceil)  and int(i[0]) > int(tbase):
                t = reltime(i[0] , tbase )
                tree.insert( t )
                tree.find(t).set_gtu(float(i[1]))
    return tree

def maximum(node):
    current = node
    while current.right is not None:
        current = current.right
    return current
def predecessor(node):
    if node.left is not None:
        return maximum(node.left)
    current = node
    while current.parent is not None and current.parent.left is current:
        current = current.parent
    if current.parent == None:
        return bst.BSTnode(None, None)
    return current.parent


def dyna_int_updater(IntValue,tdo,tup,innode,nxsmaller,nxlarger):
    if nxsmaller.key == None :
        smallerkey = 0 
    else :
        smallerkey = nxsmaller.key
    if nxlarger.key == None and smallerkey!= 0 :
        largerkey = abs(reltime( tup , tdo) )
    elif nxlarger.key == None and smallerkey == 0 :
        largerkey = abs(reltime( tup , tdo))
    else :
        largerkey = nxlarger.key
    ################
    if nxsmaller.key != None and nxlarger.key != None:
        fark = abs( (largerkey - innode.key) * nxsmaller.get_gtu() ) / 3600
    elif nxsmaller.key == None :
        fark = abs( (largerkey - smallerkey) * nxlarger.get_gtu() ) / 3600
    elif nxlarger.key == None : 
        fark = abs( (largerkey - smallerkey) * nxsmaller.get_gtu() ) / 3600
    else :
        fark = IntValue
    ##################
    IntValue -=  fark
    #################
    if nxsmaller.key != None and nxlarger.key != None:
        newarea = (abs( (largerkey - innode.key) ) * innode.get_gtu() ) / 3600
    elif nxsmaller.key == None :
        newarea = (abs( (innode.key - smallerkey)) * innode.get_gtu() + abs((largerkey - innode.key)) * innode.get_gtu() ) / 3600
    elif nxlarger.key == None :
        newarea = newarea = (abs((innode.key - smallerkey)) * nxsmaller.get_gtu() + abs((largerkey - innode.key) * innode.get_gtu()) ) / 3600
    else : 
        newarea = (abs( (largerkey - innode.key) ) * innode.get_gtu() ) / 3600
        
    IntValue += newarea
    return IntValue

def GTU_tree_rad_calc(MTree,tlo= None, thi= None, tbase="070000", tceil="220000"):
    t1 = time.perf_counter_ns()
    intlist = []
    if tlo == None :
        tlo = tbase
    if thi == None :
        thi = tceil
    node = MTree.root.minimum()
    x1 = reltime(tlo , tbase)
    if node.successor().key == None:
        x2 = reltime(tlo , thi)
    else:
        x2 = node.successor().key
    while True:
        if node.key >= reltime(tlo,tbase) and node.key <= reltime (thi , tbase):
            if x2 > reltime(thi,tbase):
                x2 = reltime(thi,tbase)
            y = node.get_gtu()
            if len(intlist) >= 1:
                integral = abs((x2 - x1) * y / 3600 + intlist[-1] )
            else :
                integral = abs ((x2 - x1) * y / 3600 )
            intlist.append( integral ) 
            
            if node.successor().key == None or node.successor().key > reltime(tceil , tbase):
                break
            else : 
                node = node.successor()
                x1 = x2
                if node.successor().key == None:
                    x2 = reltime (thi , tlo) 
                else:
                    x2 = node.successor().key
        else :
            if node.successor().key == None or node.successor().key > reltime(tceil , tbase):
                break
            else : 
                node = node.successor()
                #x1 = x2
                if node.successor().key == None:
                    x2 = reltime (thi , tlo) 
                else:
                    x2 = node.successor().key
    t =  time.perf_counter_ns() - t1
    return intlist[-1], intlist ,t

def GTU_int_calc(filename, TreeType, tlo=None, thi=None, tbase="070000", tceil="220000"):
    if tlo == None :
        tlo = tbase
    if thi == None :
        thi = tceil
    t1 = time.perf_counter_ns()
    ##############
    fvalues = open(filename , "r")
    a = fvalues.read()
    values = a.strip().split('\n')
    fvalues.close()
    l = []
    intlist = []
    for i in values:
        l.append(i.strip().split())
    count = 0
    if TreeType == 'BST':
        tree = bst.BST()
        for i in l:
            if int(i[0]) < int(tceil)  and int(i[0]) > int(tbase):
            
                t = reltime(i[0] , tbase )
                tree.insert( t )
                node = tree.find(t)
                node.set_gtu(float(i[1]))
                if count == 0 :
                    intvalue = GTU_tree_rad_calc(tree,tlo, thi, tbase , tceil)[0]
                else :
                    intvalue = dyna_int_updater(intvalue,tlo,thi,node,predecessor(node),node.successor())
                count = 1
                intlist.append(intvalue)
    elif TreeType == 'AVL':
        tree = avl.AVL()
        for i in l:
            if int(i[0]) < int(tceil)  and int(i[0]) > int(tbase): 
                t = reltime(i[0] , tbase )
                tree.insert( t )
                tree.find(t).set_gtu(float(i[1]))
                intvalue = GTU_tree_rad_calc(tree,tlo, thi, tbase , tceil)[0]
                if count == 0 :
                    intvalue = GTU_tree_rad_calc(tree,tlo, thi, tbase , tceil)[0]
                else :
                    intvalue = dyna_int_updater(intvalue,tlo,thi,tree.find(t),predecessor(node),node.successor())
                count = 1
                intlist.append(intvalue)
    
    
    t = time.perf_counter_ns() - t1
    return intvalue , intlist , t

def GTU_tree_dyna_add(filename, MTree, IntValue=0, tlo=None, thi=None,tbase="070000", tceil="220000") :
    t1 = time.perf_counter_ns()
    fvalues = open(filename , "r")
    a = fvalues.read()
    values = a.strip().split('\n')
    fvalues.close()
    intlist = []
    l = []
    intvalue = GTU_tree_rad_calc(MTree,tlo, thi, tbase, tceil)[0]
    for i in values:
        l.append(i.strip().split())
    for i in l:
        
        if int(i[0]) < int(tceil)  and int(i[0]) > int(tbase):
        
            t = reltime(i[0] , tbase )
            
            MTree.insert( t )
            node = MTree.find(t)
            
            node.set_gtu(float(i[1]))
            intvalue = dyna_int_updater(intvalue,tlo,thi,node,predecessor(node),node.successor())
            intlist.append(intvalue)
    
    t = time.perf_counter_ns() - t1
    return intvalue, intlist , t

        
    
        
    
