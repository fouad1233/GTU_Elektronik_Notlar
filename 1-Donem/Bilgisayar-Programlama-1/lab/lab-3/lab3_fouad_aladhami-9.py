# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:00:19 2021

@author: Fouad Aladhami
"""
'''
Lab Submission

General template for labs and problems:
1. You should define a function for each problem.
2. Your functions should return the expected output. Not print it.
3. Function names should be problem names such as:
   `problem1`, `problem2`, `problem3`, etc.
4. Do not forget to change the three variables called `my_name`, `my_id`, and `my_email`.
   Do NOT erase these variables or you will receive 0.
5. Make sure to execute this code and observe the outputs. If something does
   not work there, you will receive a 0 for the broken parts.
6. Respect the indentation. Each problem should have its own indentation.
7. Remove pass statements when you implement your function
'''

my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"


#Problem 1 - Find the King[3 pts]
def problem1( x ):
    if "K" in str(x):
        return True
    else:
        return False
#Problem 2 - Minimum of the four[6 pts]    
def problem2( a , b , c , d) :
    x = min(a , b , c , d )
    return x
#Problem 3 - Round to the nearest[8 pts]
def problem3( a , b):
    
    if a < b and int(a) == 0 and a < 0 and (1 + b) < -b and int(b) == 0:
        return ( -1 )
    elif a == b and a < -1 and abs(a - int(a) ) == 0.5:
        return ( int(a) - 1)
    elif int(a) == a:
        return a
    elif a < 0 and b < 0 and abs(b - int(b)) == 0.5 and a > b :
        return ( int(a) - 1)
    elif    a < 0 and b < 0 and a < b :
        return ( int(a)  )
    elif a < 0 and b > 0 and int(a) == 0:
        return 0
    elif a < 0 and b < a and int(a) == 0:
        return -1
    elif    abs(int(a) -b) >= abs(int(a+ 1) -b) and a < 0 and a == b and int(a) == 0 and a > -0.5  :
        return (int(a) )
    
    elif    abs(int(a) -b) <= abs(int(a+ 1) -b)  and a < b and a < 0 and b < 0 :
        return ( int(a) - 1)
    elif    abs(int(a) -b) >= abs(int(a+ 1) -b) and a < 0  :
        return (int(a) - 1)
    elif    abs(int(a) -b) >= abs(int(a+ 1) -b) and a > 0  :
        return (int(a) + 1)
    elif    abs(int(a) -b) < abs(int(a+ 1) -b) :
        return ( int(a)  )
    
    elif b > a and a > 0:
        return (int(a) + 1 )
    
    elif b > a and int(a) == 0 and a < 0:
        return ( 0 )
    
#Problem 4 - Volume of a cylinder[5 pts]    
def problem4(radius, height, pi=3.1415 ):
    volume = height * pi * radius ** 2
    return volume
#Problem 5 - Volume of a cylinder with error check[7 pts]
def problem5(radius, height, pi=3.1415 ):
    
    if type(radius) != type(1) and type(radius) != type(1.2) or type(height) != type(1) and type(height) != type(1.2) or type(pi) != type(1) and type(pi) != type(1.2) :
        return -1
    else:
        
        return height * pi * radius ** 2


#Problem 6 - Mr. Lonely[15 pts]
def problem6(string):
    d={}
    
    for i in string:
        d[i] = 0
    for i in string:
        d[i] = d[i] + 1
    
    for i in string:
        
        if (d[i] == 1):
            return i
        
        
    
 


      
#Problem 7 - Ascending ordered string[13 pts]  
def problem7(s):
    n = len(s)
 
    # create a character array
    # of the length of the string
    c = [s[i] for i in range(len(s))]
 
    # sort the character array
    c.sort(reverse = False)
 
    # check if the character array
    # is equal to the string or not
    for i in range(n):
        if (c[i] != s[i]):
            return False
         
    return True
#Problem 8 - Unique characters[14 pts]
def problem8(st):
    st = sorted(st)
 
    for i in range(len(st)-1):
 
        # if at any time, 2 adjacent
        # elements become equal,
        # return false
        if (st[i] == st[i + 1]) :
            return False
             
    return True
#Problem 9- Recurse with me[13 pts]
def problem9(row,column):
    if row == 1 and column ==1:
        return 1
    elif column == 1 and row > 1:
        return 3
    elif column == row and row > 1:
        return 2
    else:
        a = row - 1
        b = column -1 
        return (problem9(a , b) + problem9(a,column))
    
    
def problem10(x , y):
    count=0
    lenghx = len(x)
    lenghy = len(y)
    say = 0
    for i in range( min( lenghx ,lenghy )-1):
        
        
        
        
        
        if x[say] == y[say]:
            print(x[say])
            count = count + 1
        say +=1
    if x[-1] == y[-1]:
        print(x[-1])
        count = count + 1
    return count
            

    
    
        
    

# Define a function for each problem given in the assignment


# This is what will be called when you execute your program.
# Below this line will not show up when you are graded
# This area is used for you to test your programs.
# So make sure to test your functions here
if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")

    # We run the print on the function since we will be returning the value
    # and print() function will print whatever is passed within its parentheses.
    print("Running problem 1")
    print( problem1(67676) )

    print("Running problem 2")
    print( problem2(2.3, -2.4, -1, 4.3) )
    
    print("Running problem 3")
    print( problem3(3.2, 10) )
    
    print("Running problem 4")
    print( problem4(radius=2, height=3) )
    
    print("Running problem 5")
    print( problem5(radius="test", height=3) )
    
    print("Running problem 6")
    print( problem6("1223"))

    print("Running problem 7")
    print( problem7("abc") )
    
    print("Running problem 8")
    print( problem8("abc") )
    
    print("Running problem 9")
    print( problem9(9, 1) )
    
    print("Running problem 10")
    print( problem10("kesitT","kelasT") )
    
    
