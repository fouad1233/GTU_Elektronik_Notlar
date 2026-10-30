# -*- coding: utf-8 -*-
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


#Problem1-Fahrenheit-Celsiusconversion[6pts]
def problem1():
    x = float(input("Enter Fahrenheit degree: "))
    celsiyus = (x - 32)*(5 / 9)
    return celsiyus
#Problem2-Celsius-Fahrenheitconversion[6 pts]
def problem2():
    y = float(input("Enter Celsius degree: "))
    fahrenheit = y * ( 9 / 5 ) + 32
    return fahrenheit
#Problem3-Hexagonal number[7 pts]
def problem3():
    n = int(input("Enter a number: ") )
    h = 2*(n**2) - n
    return h
#Problem4-Lucas number[14 pts]
def problem4():
    n = int(input("Enter a number: "))
    a = 2
    b = 1
    if n == 0:
        return a
    elif n == 1:
        return b
    elif n > 0:
        #this loop change variables and add the 2 number beforne n .
        for i in range(1,n):
            c = 0
            c = a + b 
            a = b
            b = c
    return b
    
#Problem5-Reversing a string[3 pts]
def problem5():
    string = input("Enter a string: ")
    a = string[ :  : -1]
    return a
#Problem6-Removing unwanted printable characters[11 pts]
def problem6():
    x = input("Enter a string: :")
    list1= """!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~"""
    s = ""
    for i in x:
        if i in list1:
            continue
    #else:
    
        s += i # s = s + i
    return(s)
        
#Proablem7-Base 4 representation[13 pts]
def problem7():
    target = int(input("Enter input: "))
    s = ""
    if target < 0:
        y = "-"
    else:
        y = ""
    while True :
        if target == 0  :
            break
        else:
            if target < 0:
                target = target * -1
            s += str(target % 4)
            target = target // 4
            sayi = s[::-1]
            # target = int(target / 2)
            
    return y + sayi
#Problem8-Valid brackets[15 pts]
def problem8():
	a = input("Enter input: ")
	open_list = ["[","{", "("]
	close_list = ["]", "}", ")"]
	o = []
	c = []
	flag = False

	for i in a:
		if i in open_list:
			o += i
		elif i in close_list:
			c += i


	if len(o) == len(c):
		for i in range(len(o)):
			if open_list.index(o[i]) == close_list.index(c[i]):
				flag = True 

	return flag
            

    
def problem9():
    x = str(input("Enter a string: "))
    count = 0
    lengh = len(x) -1
    while(lengh != 0):
        if( x[-1 * count] == ' '):
            return count - 1 ;
        else:
            count += 1;
            lengh -= 1;
    return count + 1;
#Problem10- Escape the maze[14 pts]   
def problem10():
    route = str(input("Enter the exit route: "))
    x = 0
    y = 0
    n = 0
    for i in range(1,len(route) + 1):
         
        if route[n] == "e":
            x = x + 1
            n += 1
        elif route[n] == "w":
            x = x - 1
            n += 1
        elif route[n] == "n":
            y = y + 1
            n += 1
        elif route[n] =="s":
            y = y - 1
            n += 1
        else:
            return
        
    value = (x**2 + y**2)
    
    guess = float("1")
    while value != guess**2 :
        guess = (1 / 2)*(guess + value / guess )
        if guess == (1 / 2)*(guess + value / guess ):
            break
    return guess
    
        
            
            
    
            
        
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
    print( problem1() )

    print("Running problem 2")
    print( problem2() )
    
    print("Running problem 3")
    print( problem3() )
    
    print("Running problem 4")
    print( problem4() )
    
    print("Running problem 5")
    print( problem5() )
    
    print("Running problem 6")
    print( problem6() )
    
    print("Running problem 7")
    print( problem7() )
    
    print("Running problem 8")
    print( problem8() )
    
    print("Running problem 9")
    print( problem9() )
    
    print("Running problem 10")
    print( problem10() )
    
    
    
