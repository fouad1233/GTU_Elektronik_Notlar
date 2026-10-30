#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  5 13:15:21 2022

@author: fuad
"""
'''#1stlecture
type(5)
print(3.0-1)
Python vs. Math

# Which is allowed in Python?

# Exercise 2
'''
'''
# x + y = 2
# x*x = 2
# 2 = x
#[correct below]
xy = 2;
# None of the Above
'''
'''
#exersice 3
usa_gold = 46
uk_gold = 27
romania_gold = 1

total_gold = usa_gold + uk_gold + romania_gold
print(total_gold)

romania_gold += 1
print(total_gold)
'''
#lectue2
'''
# Strings

# What is the value of variable `u` from the code below?

once = "umbr"
repeat = "ella"
u = once + (repeat+" ")*4
'''

'''
# Comparisons

# What does the code below print?

pset_time = 15
sleep_time = 8
print(sleep_time > pset_time)
derive = True
drink = False
both = drink and derive
print(both)
#print False then False
'''

'''
# Branching

# What's printed when x = 0 and y = 5?

x = float(input("Enter a number for x: "))
y = float(input("Enter a number for y: "))
if x == y:
    if y != 0:
        print("x / y is", x/y)
elif x < y:
    print("x is smaller")
else:
    print("y is smaller")
'''
'''
# While Loops

# In the code below from Lecture 2, what is printed when you type "Right"?
n = input("You're in the Lost Forest. Go left or right? ")
while n == "right":
    n = input("You're in the Lost Forest. Go left or right? ")
print("You got out of the Lost Forest!")
# You got out of the Lost Forest! printed
'''

'''
# For Loops

# What is printed when the below code is run?

mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
        mysum += 1
print(mysum)

'''
#Lecture 3
'''
# 1.String Manipulations
# What does the code below print?

s = "6.00 is 6.0001 and 6.0002"
new_str = ""
new_str += s[-1]
new_str += s[0]
new_str += s[4::30]    
new_str += s[13:10:-1]
print(new_str)
#'26 100' is printed
'''
'''
# 2.For Loops with Strings
# How many times will the code below print "common letter"?

s1 = "mit u rock"
s2 = "i rule mit"
if len(s1) == len(s2):
    for char1 in s1:
        for char2 in s2:
            if char1 == char2:
                print("common letter")
                break
'''
#lecture 4
'''
# 1.Function Calls

# How many total lines of output will show up if you run the code below?
def add(x, y):
    return x+y

def mult(x, y):
    print(x*y)

add(1,2) #this return 3
print(add(2,3)) # this print 5
mult(3,4) # this return 12
print(mult(4,5)) #this return None 
'''

'''
# 2. Functions as Arguments

# What does the code below print?

def sq(func, x):
    y = x**2
    return func(y)

def f(x):
    return x**2

calc = sq(f, 2)
print(calc)
'''
#lectue 5 
'''
# 1.Tuples

# Examine the code below. What does always_sunny(('cloudy'), ('cold',)) evaluate to?

def always_sunny(t1, t2):
    """ t1, t2 are non empty """
    sun = ("sunny","sun")
    first = t1[0] + t2[0]
    return (sun[0], first)
#The trick here t1 type is string 
'''

'''
# 2.Simple Lists

# What is the value of L after you run the code below?

L = ["life", "answer", 42, 0]
for thing in L:
    if thing == 0:
        L[thing] = "universe"
    elif thing == 42:
        L[1] = "everything"
'''
'''
#important
L = ['universe', 'everything', 42, 0]

L.extend('123')

L
#Out[55]: ['universe', 'everything', 42, 0, '1', '2', '3']

'''
'''
#3. List Operations

# What is the value of L3 after you execute all the operations in the code below?

L1 = ['re']
L2 = ['mi']
L3 = ['do']
L4 = L1 + L2
L3.extend(L4)
L3.sort()
del(L3[0])
L3.append(['fa','la'])
print(L3)
#Out[57]: ['mi', 're', ['fa', 'la']]
'''

'''
# 4.List Aliasing/Mutation

# What is the value of brunch after you execute all the operations in the code below?

L1 = ["bacon", "eggs"]
L2 = ["toast", "jam"]
brunch = L1
L1.append("juice")
brunch.extend(L2)
print(brunch)
#Out[59]: ['bacon', 'eggs', 'juice', 'toast', 'jam']
'''
#Lecture 7
#even çift demek

'''
#1.Black Box and Glass Box Testing

# With the below implementation, is the test set "n = 4 | n = -4 | n = 5" path complete?

def is_even(n):
    """ 
    Returns True if a number is even
    and False if not 
    """
    if n > 0 and n % 2 == 0:
        return True
    elif n < 0 and n % 2 == 0:
        return True
    else: 
        return False
# Exercise 1
# [correct]Yes&nbsp;
# No

# With the above implementation, which value for n is incorrectly labeled by is_even?

# Exercise 2
# n is very large (and positive)
#  n is very small (and negative)
# [correct]n is 0&nbsp;
'''
'''
# 2.Errors

# Below is a piece of code and an error shown when running it. What is the problem?

L = 3
for i in range(len(L)):
    print(i)

# ERROR MESSAGE:

#  File "C:/Users/Ana/.spyder2-py3/temp.py", line 2, in 
#     for i in range(len(L)):

# TypeError: object of type 'int' has no len()

# Exercise 3
# You are not allowed to name an integer with the variable name L
# range is not allowed to have an expression inside its parentheses
# [correct]You are not allowed to call len on an integer&nbsp;
# You are not allowed to print the loop variable i
'''

'''

# 3. Exceptions
# If the user enters "twenty" in the code below what does the program do?


try:
    n = int(input("How old are you? "))
    percent = round(n*100/80, 1)
    print("You've gone through", percent, "% of your life!")
except ValueError:
    print("Oops, must enter a number.")
except ZeroDivisionError:
    print("Division by zero.")
except:
    print("Something went very wrong.")



# Exercise 4
# prints "You've gone through 25.0 % of your life!"
# [correct]prints "Oops, must enter a number."&nbsp;
# If the user enters "0" in the code above what does the program do?

# Exercise 5
# [correct]prints "You've gone through 0.0 % of your life!"&nbsp;
# prints "Division by zero."
'''

#lecture8
'''
# Class Definition

# Which of the following is a good and valid definition for a class representing a car?

# Exercise 1
# def class Car(object):
# [correct]class Car(object):&nbsp;
# def Car(object):
# class A(object)
'''

'''
# 2.Class Instance

# Using the class definition below, which line creates a new Car object with 4 wheels and 2 doors?

class Car(object):
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""
#  Exercise 2
# Car(mycar, 4, 2)
# mycar = Car(4, 2, "white")
# [correct]mycar = Car(4, 2)&nbsp;
# mycar = Car(2, 4)
'''
'''
# 3.Methods

# Which of the following methods changes the color of the car, based on the definition below?

class Car(object):
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""
 # Exercise 3
 #   def paint(c):
 #    color = c
 #   def paint(self, c):
 #    color = c
 #   def paint(c):
 #    self.c = c
# [correct]
    def paint(self, c):
        self.color = c

'''

'''
# 4.Method Call

# You create a car with mycar = Car(4, 2). Which is a line of code to change the color of mycar to "red"?

class Car(object):
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""
    def paint(self, c):
        self.color = c
#  Exercise 4
# Car.paint("red")
# mycar.paint(red)
# [correct]mycar.paint("red")&nbsp;
# mycar.paint(Car, "red")
'''

'''
# 5.Special Methods

# With the code below, what does the line print(mycar == yourcar) print?

class Car(object):
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""
    def paint(self, c):
        self.color = c
    def __eq__(self, other):
        if self.wheels == other.wheels and \
            self.color == other.color and \
            self.doors == other.doors:
            return True
        else:
            return False

mycar = Car(4, 2)
mycar.paint("red")
yourcar = Car(4,2)
print(mycar == yourcar)

'''
#lecture 9
'''
# 1.Getters and Setters

# Which of the below is a getter method for the number of wheels?

# ----------------------------------
# ----------- Given ------------
# ----------------------------------
class Car(object):
    def __init__(self, w, d):
        self.wheels = w
        self.doors = d
        self.color = ""
# ----------------------------------

# (A)    def get_wheels():
#              return wheels

# (B)    def get_wheels():
#              return self.wheels

# (C)    def get_wheels(self):
#              return wheels

# (D)    def get_wheels(self):
#              return self.wheels #correct

'''






















