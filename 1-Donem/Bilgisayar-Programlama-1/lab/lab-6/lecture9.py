# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 14:33:24 2021

@author: fcayci
"""
'''
sayiyi hexe cevirme

'{:06x}'.format(127)
'''

"""
# class Coord(object):
class Coord:
    
    def __init__(self, x, y):
        
        print("Hello from init")
        self.x = x
        self.y = y
        
    def distance_from_origin(self):
        return (self.x**2 + self.y**2)**0.5
    
    def distance(self, other):
        
        return ((self.x - other.x)**2 +
        (self.y - other.y)**2)**0.5
        
    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'
      
    def __add__(self, other):
        yenix = self.x + other.x
        yeniy = self.y + other.y
        return Coord(yenix, yeniy)
    
    def __len__(self):
        return 2
    
    """
"""
class Fraction():
    
    def __init__(self, n, d):
        self.nomin = n
        self.denom = d
    
    def __str__(self):
        return str(self.nomin) + "/" + str(self.denom)
    
    def get_deger(self):
        return self.nomin / self.denom
    
 """

class Kume:
     
    def __init__(self):
        self.vi = []

    def __str__(self):
        self.vi.sort()
        return '<' + str(self.vi)[1:-1] + '>'
    
    def __len__(self):
        return len(self.vi)

    def ekle(self, val):
        if isinstance(val, int): 
            if not val in self.vi:
                self.vi.append(val)
        else:
            raise ValueError("not an int")
 
    def cikar(self, val):
        try:
            self.vi.remove(val)
        except ValueError:
            print("not in the list")
 
    def __add__(self, other):
        x = Kume()
        print(x)
        for i in self.li:
            x.ekle(i)    
            print(x)
        for i in other.li:
            x.ekle(i)    
            print(x)
        return x
    
    
 
x1 = Kume()
x1.ekle(4)
x1.ekle(5)
x1.ekle(4)
x1.ekle(1)
print(x1) 
 

x2 = Kume()
x2.ekle(1)
x2.ekle(5)
x2.ekle(7)
x2.ekle(9)
print(x2)


'''
class INF211:
    
    def __init__(self, x=3):
        self.x = x
        
    # getter
    def get_x(self):
        return self.x
    
    # setter
    def set_x(self, x):
        self.x = x
'''
 
 