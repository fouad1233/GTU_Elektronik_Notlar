#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:50:48 2022

@author: fuad
"""
import avlgtu as avl , hashlib
my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"
def problem1(file):
    try:
        text = open(file, "r")
        f = text.read()
        lofst = f.strip().split('\n')
        text.close()
        lofavl = []
        for element in range(4096):
            lofavl.append(avl.AVL())
        for i in lofst:
            li = i.strip().split()
            plate = li[0] + li[1] + li[2]
            md5 = hashlib.md5()
            md5.update(plate.encode())
            hexcode = md5.hexdigest()
            deci = int(hexcode[len(hexcode) - 3: len(hexcode):], 16)
            lofavl[deci].insert(plate)
            node = lofavl[deci].find(plate)
            node.color = li[3]
            node.fuel = li[4]
            node.engine = li[5]
        return lofavl
    except :
        return None 
class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        if self.adj[u] is None:
            self.adj[u] = []
        self.adj[u].append(v)
from collections import deque
class BFSResult:
    def __init__(self):
            self.level = {}
            self.parent = {}
def bfs(g, s):
    
    """Queue-based implementation of BFS.
    Args:
        g: a graph with adjacency list adj such that g.adj[u] is a list of u’s
           neighbors.
        s: source.
    """
    r= BFSResult()
    r.parent = {s: None}
    r.level = {s: 0}
    
    queue = deque()
    queue.append(s)
    #print(queue)
    
    while queue:
        u = queue.popleft()
        #print(u)
        #print(g.adj[u])
        if g.adj[u] != None:
            for n in g.adj[u]:
                #print(u)
                if n not in r.level:
                    r.parent[n] = u
                    r.level[n] = r.level[u] + 1
                    queue.append(n)
    return r 
def problem2(vertices, edges):
    try : 
        obj = Graph()
        for u in vertices:
            obj.adj[u] = None
            for li in edges:
                for v in li :
                    
                    if v == u : 
                        for i in li :
                            if i != u :
                                obj.add_edge(u, i)
        return obj
    except: 
        return None 
def problem3(vertices, edges):
    try : 
        obj = Graph()
        for u in vertices:
            obj.adj[u] = None
            for li in edges:
                if li[0] == u:
                    obj.add_edge(u, li[1])
        return obj
    except : 
        return None
def problem4(g , s):
    try : 
        return bfs(g,s)
    except:
        return None
def problem5(Vertices,Edges,s,o,direction):
    try : 
        if direction == "u":
           G = problem2(Vertices,Edges) 
        elif direction == "d":
            G = problem3(Vertices,Edges) 
        else :
            return None
        B = problem4(G,s)
        parentdict = B.parent
        li_from_o_to_s = []
        element = parentdict[o]
        li_from_o_to_s.append(o)
        li_from_o_to_s.append(element)
        while element != s:
            if element == None or element not in B.parent :
                return "INF212"
            element = parentdict[element]
            li_from_o_to_s.append(element)
        li_from_s_to_o = li_from_o_to_s[::-1]
        return li_from_s_to_o
    except KeyError:
        return "INF212"
    except :
        return None