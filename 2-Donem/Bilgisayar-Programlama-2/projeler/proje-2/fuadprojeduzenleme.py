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
 
        # Mark the current node as visited
        visited[v]= True
 
        # Recur for all the vertices
        # adjacent to this vertex
        if self.adj[v] != None : 
            for i in self.adj[v]:
                 
                # If the node is not
                # visited then recurse on it
                if  visited[i]==False :
                    if(self.isCyclicUtil(i,visited,v)):
                        return True
                # If an adjacent vertex is
                # visited and not parent
                # of current vertex,
                # then there is a cycle
                elif  parent!=i:
                    return True
             
            return False
          
  
    # Returns true if the graph
    # contains a cycle, else false.
    def isCyclic(self):
       
        # Mark all the vertices
        # as not visited
        visited  = {}
        for i in self.vertices:
            visited[i] = False
        
        # Call the recursive helper
        # function to detect cycle in different
        # DFS trees
        for i in self.vertices:
           
            # Don't recur for u if it
            # is already visited
            if visited[i] ==False:
                if(self.isCyclicUtil(i,visited,-1)) == True:
                    return True
         
        return False
    def isCyclicUtild(self, v, visited, recStack):
    
        # Mark current node as visited and
        # adds to recursion stack
        visited[v] = True
        recStack[v] = True
    
        # Recur for all neighbours
        # if any neighbour is visited and in
        # recStack then graph is cyclic
        if self.adj[v] != None : 
            for neighbour in self.adj[v]:
                if visited[neighbour] == False:
                    if self.isCyclicUtild(neighbour, visited, recStack) == True:
                        return True
                elif recStack[neighbour] == True:
                    return True
            
            # The node needs to be popped from
            # recursion stack before function ends
            recStack[v] = False
            return False
    
    # Returns true if graph is cyclic else false
    def isCyclicd(self):
        visited = [False] * (len(self.vertices) + 1)
        recStack = [False] * (len(self.vertices) + 1)
        for node in self.vertices :
            if visited[node] == False:
                if self.isCyclicUtild(node,visited,recStack) == True:
                    return True
        return False
    def topologicalSortUtil(self, v, visited, stack):
    
        # Mark the current node as visited.
        visited[v] = True
    
        # Recur for all the vertices adjacent to this vertex
        if self.adj[v] != None : 
            for i in self.adj[v]:
                if visited[i] == False:
                    self.topologicalSortUtil(i, visited, stack)
        
            # Push current vertex to stack which stores result
            stack.append(v)
        else :
            stack.append(v)
    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*len(self.vertices)
        stack = []
    
        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in self.vertices:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
        return stack[::-1]
def Dir_cyclic_or_acyclic(gr):
    if gr.gtype == "u":
        return None

    return gr.isCyclicd()
def UnDir_cyclic_or_acyclic(gr):
    if gr.gtype == "d":
        return None
    return gr.isCyclic()
def T_sort(gr) :
    if gr.gtype != "d" or Dir_cyclic_or_acyclic(gr) != False :
        return None
    return gr.topologicalSort()


