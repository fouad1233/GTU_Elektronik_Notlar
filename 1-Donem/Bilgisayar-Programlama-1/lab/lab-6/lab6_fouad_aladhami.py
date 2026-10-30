#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 15:09:02 2021

@author: fuad
"""

my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"

def problem0():
    '''Doctests
    >>> A = problem0()
    >>> ainst = A(3)
    >>> ainst.get_value()
    3
    >>> A = problem0()
    >>> ainst = A(1)
    >>> ainst.get_value()
    1
    >>> A = problem0()
    >>> ainst = A(-4)
    >>> ainst.get_value()
    -4
    >>> ainst.set_value(5)
    >>> ainst.get_value()
    5
    '''

    # p0 class is defined inside the function
    # if name is given in the problem, use that name as the class name.
    # If name is NOT given in the problem, pick a name yourself.
    # For example, you can just use p# structure.
    class p0:

        # These are class members. Make sure your indentation is correct.
        def __init__(self, x):
            self.a = x

        def get_value(self):
            return self.a

        def set_value(self, x):
            self.a = x

    # Make sure to always return the class
    # Otherwise we will not see it (i.e. NoneType),
    # and your problem will be marked 0.
    return p0
def problem1():
    """
    
    >>> A = problem1()
    >>> ainst = A(3.5)
    >>> ainst.get_value()
    0
    >>> A = problem1()
    >>> ainst = A([1])
    >>> ainst.get_value()
    0
    >>> A = problem1()
    >>> ainst = A(None) # Creating an instance with None as parameter
    >>> ainst.get_value()
    0
    >>> A = problem1()
    >>> ainst = A(-4)
    >>> ainst.get_value()
    -4
    >>> ainst.set_value(7.6)
    >>> ainst.get_value()
    -4
    >>> ainst.set_value(3)
    >>> ainst.get_value()
    3


    """
    class p1:
        
        def __init__(self,x):
            self.a = x
        
        def get_value(self):
            if  isinstance(self.a , int) :
                
                return self.a
            else :
                self.a = 0
                return self.a
        def set_value(self, x):
            if isinstance(x , int):
                self.a = x
            else :
                pass

    return p1

def problem2():
    '''
    

    >>> A = problem2()
    >>> ainst = A(3, 5)
    >>> ainst.get_area()
    15
    >>> ainst.get_perimeter()
    16
    '''
    class p1:
        def __init__(self , x , y):
            self.x = x
            self.y = y
        def get_area(self):
            
            return self.x * self.y
        def get_perimeter(self):
            return 2*self.x + 2*self.y
        
    return p1
def problem3():
    """
    
    >>> A = problem3()
    >>> ainst = A()
    >>> ainst.get_min()
    0.0
    >>> ainst.get_max()
    0.0
    >>> ainst.get_mean()
    0.0
    >>> ainst.get_median()
    0.0
    >>> ainst.add_grade(3)
    >>> ainst.add_grade(5)
    >>> ainst.get_min()
    3.0
    >>> ainst.get_max()
    5.0
    >>> ainst.get_mean()
    4.0
    >>> ainst.get_median()
    4.0
    >>> ainst.add_grade(10)
    >>> ainst.get_min()
    3.0
    >>> ainst.get_max()
    10.0
    >>> ainst.get_mean()
    6.0
    >>> ainst.get_median()
    5.0
    >>> ainst.remove_grade(15)
    >>> ainst.remove_grade(10)
    >>> ainst.get_min()
    3.0
    >>> ainst.get_max()
    5.0
    >>> ainst.get_mean()
    4.0
    >>> ainst.get_median()
    4.0
    """
    class Grades:
        def __init__(self):
            self.l = []
        def add_grade(self,x):
            self.l.append(x)
        def remove_grade(self,x):
            try :
                self.l.remove(x)
            except:
                pass
                
                
        def get_min(self):
            if len(self.l) == 0:
                return 0.0 
            
            return float(min(self.l))
        def get_max(self):
            if len(self.l) == 0:
                return 0.0 
            return float(max(self.l))
        def get_mean(self):
            if len(self.l) == 0:
                return 0.0 
            return float(sum(self.l) / len(self.l) )
        def get_median(self):
            if len(self.l) == 0:
                return 0.0 
            self.l.sort()
            if len(self.l)%2 == 1:
                return  float(self.l[ ((len(self.l)+1)//2 )-1] )
            if len(self.l)%2 == 0:
                return float(( self.l[ (len(self.l))//2 - 1] + self.l[ (len(self.l))//2] ) / 2)
            
    return Grades
def problem4():
    class Movie:
        
        def __init__(self,movie_name,director,year,rating = 0.0 ,length = 0):
            self.movie_name = movie_name
            self.director = director
            self.year = year
            self.rating = rating
            self.length = length
        def get_movie_name(self):
            return self.movie_name
        def get_director(self):
            return self.director
        def get_year(self):
            return self.year
        def get_rating(self):
            return self.rating
        def get_length(self):
            return int(self.length)
        def set_rating(self , x):
            if  isinstance(x , float) and x >= 0.0 and x <=10.0:
                self.rating = x
            else:
                pass
        def set_length(self ,x):
            if isinstance(x,int) and x >=0 and x<= 500:
                self.length = x
            else:
                pass
    return Movie
def get_board_size(board):
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    return (row ,column)
def problem5():
    '''
    >>> A = problem5()
    >>> ainst = A('movies.txt')
    >>> ainst.add_movie('The Usual Suspects', 'Bryan Singer', 1995, 8.5, 106)
    >>> ainst.get_oldest()
    'The Godfather'
    >>> ainst.get_highest_ranking()
    'The Shawshank Redemption'
    >>> ainst.get_lowest_ranking()
    'The Usual Suspects'
    >>> ainst.get_movies_by_director('Nuri Bilge Ceylan')
    []
    >>> ainst.get_movies_by_director('Francis Ford Coppola')
    ['The Godfather', 'The Godfather: Part II']

    '''
    class MovieCatalog:
        def __init__(self,filename):
            self.l = []
            f = open(filename , "r")
            
            a = f.read()
            a = a.strip().split('\n')
            new = []
            # list_dict = []
            
            for row in a:
                new.append(row.strip().split('\t'))
            
            #print(new)
            for i in range (len(new) ):
                l2 = new[i][0].strip().split(",")
                self.l.append(l2)
            
        def add_movie(self, movie_name, director, year, rating=0.0, length=0):
            if [movie_name, director, year, rating, length] not in self.l:
                self.l.append([movie_name, director, year, rating, length])
            else:
                pass
        def remove_movie(self,movie_name):
            row ,column = get_board_size(self.l)
            for i in range(row):
                if movie_name == self.l[i][0]:
                    self.l.remove(self.l[i])
        
        def get_oldest(self):
            row ,column = get_board_size(self.l)
            yearsort = []
            for i in range(row):
                yearsort.append(int(self.l[i][2]) )
            yearsort.sort()
            for i in range(row):
                if int(self.l[i][2]) == yearsort[0]:
                    return self.l[i][0]
        def get_lowest_ranking(self):
            row ,column = get_board_size(self.l)
            ranksort = []
            for i in range(row):
                ranksort.append(float(self.l[i][3]))
            ranksort.sort()
            for i in range(row):
                if float(self.l[i][3]) == ranksort[0]:
                    return self.l[i][0]
        def get_highest_ranking(self):
            row ,column = get_board_size(self.l)
            ranksort = []
            for i in range(row):
                ranksort.append(float(self.l[i][3]))
            ranksort.sort()
            for i in range(row):
                if float(self.l[i][3]) == ranksort[-1]:
                    return self.l[i][0]
        def get_movies_by_director(self,director):
            row ,column = get_board_size(self.l)
            dmovies = []
            
            for i in range(row):
                if self.l[i][1] == director:
                    dmovies.append(self.l[i][0])
            return dmovies
            
            
        # def fouad(self)  :
        #     return self.l
 
    return MovieCatalog

def problem6():
    '''
    

    >>> N = problem6()
    >>> ninst1 = N(3, 4, 5)
    >>> ninst1.get_node()
    (3, 4, 5)
    >>> res = ninst1.get_distance()
    >>> import math
    >>> math.isclose(res, 7.07, rel_tol=1e-2)
    True
    >>> print(ninst1)
    <3, 4, 5>
    >>> ninst2 = N(-2, 3, 5)
    >>> ninst3 = ninst1 + ninst2
    >>> print(ninst3)
    <1, 7, 10>
    >>> ninst2 > ninst1
    False
    >>> ninst2 >= ninst1
    False
    >>> ninst2 < ninst1
    True
    >>> ninst2 <= ninst1
    True
    >>> ninst2 == ninst1
    False
    >>> ninst2 = N(-3, 4, 5)
    >>> ninst2 == ninst1
    False
    >>> ninst2 = N(3, 4, 5)
    >>> ninst2 == ninst1
    True
    >>> ninst2 is ninst1
    False
    '''
    
    class Node:
        def __init__(self,x,y,z):
            self.x = x
            self.y = y 
            self.z = z
        def get_node(self):
            return (self.x,self.y,self.z)
        def get_distance(self):
            return ( (self.x)**2 + (self.y)**2 + (self.z)**2 )**0.5
        def __add__(self,other):
            newx = self.x + other.x
            newy = self.y + other.y
            newz = self.z + other.z
            return Node(newx,newy,newz)
        def __str__(self):
            return '<' + str(self.x) + ', ' + str(self.y)+ ', '+ str(self.z) + '>'
        #Greater than
        def __gt__(self,other):
            if  ( (self.x)**2 + (self.y)**2 + (self.z)**2 )**0.5 > ( (other.x)**2 + (other.y)**2 + (other.z)**2 )**0.5 :
                
                return True
            else :
                return False
        def __ge__(self, other):
            if  ( (self.x)**2 + (self.y)**2 + (self.z)**2 )**0.5  >= ( (other.x)**2 + (other.y)**2 + (other.z)**2 )**0.5:
                
                return True
            else :
                return False
        def __lt__(self,other):
            if  ( (self.x)**2 + (self.y)**2 + (self.z)**2 )**0.5  < ( (other.x)**2 + (other.y)**2 + (other.z)**2 )**0.5:
                
                return True
            else :
                return False
        def __le__(self,other):
            if  ( (self.x)**2 + (self.y)**2 + (self.z)**2 )**0.5  <=( (other.x)**2 + (other.y)**2 + (other.z)**2 )**0.5:
                
                return True
            else :
                return False
        def __eq__(self,other):
            if (self.x , self.y ,self.z) == (other.x , other.y ,other.z ):
                
                return True
            else :
                return False #, abs(( (self.x)**2 + (self.y)**2 + (self.z)**2 )**0.5) , abs(( (other.x)**2 + (other.y)**2 + (other.z)**2 )**0.5)
     
    return Node
def problem7():
    
    '''
    >>> A = problem7()
    >>> ainst = A(5)
    >>> nodes = ainst.get_nodes()
    >>> len(nodes)
    5
    >>> isinstance(nodes, list)
    True
    >>> isinstance(nodes[0], tuple)
    True
    >>> ainst.add_node(21, 21, 21)
    >>> nodes = ainst.get_nodes()
    >>> len(nodes)
    6
    >>> ainst.get_outermost()
    (21, 21, 21)
    >>> s = ainst.get_sum()
    >>> len(s.get_node())
    3
    '''
    
    
    
    class NodeCloud():
        def __init__(self,n):
            import random
            
            self.n = n
            self.li = []
            for i in range(self.n):
                self.li.append( (random.randint(-20, 20) , random.randint(-20 , 20) ,random.randint( -20 , 20) ) )
        def get_nodes(self):
            return self.li
        
        
        def get_outermost(self):
            l1= []
            for i in range(len(self.li) ):
                x1,y1,z1 = self.li[i]
                l1.append(problem6()(x1,y1,z1))
            l1.sort()
            return problem6().get_node(l1[-1])
        def add_node(self ,x, y, z):
            if (x,y,z) not in self.li:
                self.li.append( (x,y,z) )
            
        def get_sum(self):
            yenix = 0
            yeniy = 0
            yeniz = 0
            for i in range(len(self.li)):
                yenix += self.li[i][0]
            for j in range(len(self.li)):
                yeniy += self.li[j][1]
            for k in range(len(self.li)):
                yeniz += self.li[k][2]
            
            return problem6()(yenix , yeniy ,yeniz)
        
    return NodeCloud

def problem8():
    
    '''
    
    >>> A = problem8()
    >>> ainst = A("test")
    >>> print(ainst)
    test
    >>> ainst.morse()
    ['-', '.', '...', '-']
    >>> ainst.binary()
    '1110100110010111100111110100'
    >>> ainst.hex()
    '74657374'
    >>> ainst = A("çELık-!")
    >>> print(ainst)
    ELk
    >>> ainst.morse()
    ['.', '.-..', '-.-']
    >>> ainst.binary()
    '100010110011001101011'
    >>> ainst.hex()
    '454c6b'
    '''
    class Encoder:
        def __init__(self,x):
            self.x = ''
            allowed = set(("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"))
            for i in x:
                if i in allowed:
                    self.x +=i
        def __str__(self):
            return self.x
        def morse(self) :
            morsedict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----'}
            karakterlerim = self.x.upper()
            encoded = []
            for i in karakterlerim:
                encoded.append(morsedict[i])
            return encoded
        def binary(self):
            fouadbinary= ''
            for i in self.x:
                 fouadbinary +='{:b}'.format(ord(i))
            return fouadbinary
            
        def hex(self):
            fouadhex= ''
            for i in self.x:
                 fouadhex +='{:x}'.format(ord(i))
            return fouadhex
            
    return Encoder
if __name__ == "__main__":

    # # You can do checks like this. We will do this way.
    # A = problem0()
    # # A is the class name, and it is not the instance.
    # # We now create an intance using A
    # ainst = A(4)
    # # Now that we have the instance, we can call the methods.
    # assert 4 == ainst.get_value()
    # ainst.set_value(5)
    # assert 5 == ainst.get_value()

    # alternatively, you can set up doctests and run those
    # autocheck with doctest
    import doctest
    doctest.testmod()

    print("Completed all doctests.")

