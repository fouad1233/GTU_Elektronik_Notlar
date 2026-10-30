#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 24 12:58:46 2022

@author: fuad
"""
my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"
class Graph:
    def __init__(self):
        self.adj = {}
        self.gtype = None
        self.vertices = []
        
    def add_edge(self, u, v):
        if self.adj[u] is None:
            self.adj[u] = []
        self.adj[u].append(v)
def isCyclicUtil(self,v,visited,parent):
 
    visited[v]= True
 
    if self.adj[v] != None : 
        for i in self.adj[v]:
            if  visited[i]==False :
                if(isCyclicUtil(self, i,visited,v)):
                    return True
            elif  parent!=i:
                return True
         
    return False
def isCyclic(self):
   
    visited  = {}
    for i in self.vertices:
        visited[i] = False
    
    for i in self.vertices:
       
        if visited[i] ==False:
            if(isCyclicUtil(self , i,visited,-1)) == True:
                return True
     
    return False
def isCyclicUtild(self, v, visited, recStack):

    visited[v] = True
    recStack[v] = True

    if self.adj[v] != None : 
        for neighbour in self.adj[v]:
            if visited[neighbour] == False:
                if isCyclicUtild(self, neighbour, visited, recStack) == True:
                    return True
            elif recStack[neighbour] == True:
                return True
    recStack[v] = False
    return False
def isCyclicd(self):
    visited  = {}
    for i in self.vertices:
        visited[i] = False
    recStack = {}
    for i in self.vertices:
        recStack[i] = False
    for node in self.vertices :
        if visited[node] == False:
            if isCyclicUtild(self,node,visited,recStack) == True:
                return True
    return False
def topologicalSortUtil(self, v, visited, stack):

    visited[v] = True

    if self.adj[v] != None : 
        for i in self.adj[v]:
            if visited[i] == False:
                topologicalSortUtil(self,i, visited, stack)
    
        stack.append(v)
    else :
        stack.append(v)
def topologicalSort(self):
    visited  = {}
    for i in self.vertices:
        visited[i] = False
    stack = []
    for i in self.vertices:
        if visited[i] == False:
            topologicalSortUtil(self, i, visited, stack)
    return stack[::-1]
def Dir_cyclic_or_acyclic(gr):
    if gr.gtype != "d" :
        return None

    return isCyclicd(gr)
def UnDir_cyclic_or_acyclic(gr):
    if gr.gtype != "u":
        return None
    return isCyclic(gr)
def T_sort(gr) :
    if gr.gtype != "d" or Dir_cyclic_or_acyclic(gr) != False :
        return None
    return topologicalSort(gr)

Gu1 = Graph()
Gu1.gtype = "u"
Gu1.vertices = [4, 1, 2, 3, 5, 6]
Gu1.adj = {4: [1, 5], 1: [4, 2], 2: [1, 3, 5], 3: [2, 6], 5: [2, 6, 4], 6: [3, 5]}
print(UnDir_cyclic_or_acyclic((Gu1)))

Gu2 = Graph()
Gu2.gtype = "u"
Gu2.vertices = [1, 0, 2, 3, 4]
Gu2.adj ={1: [0, 2], 0: [1, 3], 2: [1], 3: [0, 4], 4: [3]}
print(UnDir_cyclic_or_acyclic(Gu2))

Gu3 = Graph()
Gu3.gtype = "u"
Gu3.vertices = [1, 0, 2, 3, 4]
Gu3.adj ={1: [0, 2], 0: [1, 2, 3], 2: [1, 0], 3: [0, 4], 4: [3]}
print(UnDir_cyclic_or_acyclic(Gu3))


Gd1 = Graph()
Gd1.gtype = "d"
Gd1.vertices = [4, 1, 2, 3, 5, 6]
Gd1.adj = {4: [1, 5], 1: None, 2: [1, 3, 5], 3: [6], 5: None, 6: [5]}
print(Dir_cyclic_or_acyclic(Gd1))

Gd2 = Graph()
Gd2.gtype = "d"
Gd2.vertices = [0, 1, 2, 3]
Gd2.adj ={0: [1, 2], 1: [2], 2: [3], 3: None}
print(Dir_cyclic_or_acyclic(Gd2))

Gd3 = Graph()
Gd3.gtype = "d"
Gd3.vertices = [0, 1, 2, 3]
Gd3.adj ={0: [1, 2], 1: [2], 2: [0, 3], 3: None}
print(Dir_cyclic_or_acyclic(Gd3))
            
Gd4 = Graph()
Gd4.gtype = "d"
Gd4.vertices = [0, 1, 2, 3]
Gd4.adj ={0: [1, 2], 1: [2], 2: [3], 3: [3]}
print(Dir_cyclic_or_acyclic(Gd4))

Gd1 = Graph()
Gd1.gtype = "d"
Gd1.vertices = [4, 1, 2, 3, 5, 6]
Gd1.adj = {4: [1, 5], 1: None, 2: [1, 3, 5], 3: [6], 5: None, 6: [5]}
print(T_sort(Gd1))

Gd2 = Graph()
Gd2.gtype = "d"
Gd2.vertices = [0, 1, 2, 3]
Gd2.adj ={0: [1, 2], 1: [2], 2: [3], 3: None}
print(T_sort(Gd2))

Gd3 = Graph()
Gd3.gtype = "d"
Gd3.vertices = [0, 1, 2, 3]
Gd3.adj ={0: [1, 2], 1: [2], 2: [0, 3], 3: None}
print(T_sort(Gd3))            
Gd4 = Graph()
Gd4.gtype = "d"
Gd4.vertices = [0, 1, 2, 3]
Gd4.adj ={0: [1, 2], 1: [2], 2: [3], 3: [3]}
print(T_sort(Gd4))       


