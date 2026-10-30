my_name = "Fouad Aladhami"
my_id = 99836783058
my_email = "f.aladhami2021@gtu.edu.tr"

#Problem 1 -Greeting I
def problem1():
    my_name = "Fouad Aladhami!"
    a = "Hi all, This is "+ my_name
    return (a)
    
#Problem 2 -Greeting II
def problem2():
    enterinput = str( input("Enter some input: ") )
    b = "Input was "+ enterinput
    return (b)

#Problem 3-Addition
def problem3():
    first_number = int( input("Enter first number: ") )
    second_number = int( input("Enter second number: ") )
    c = first_number + second_number
    return (c)

#Problem 4-Subtraction
def problem4():
    first_numberr = float( input("Enter first number: ") )
    second_numberr = float( input("Enter second number: ") )
    d = first_numberr - second_numberr
    return (d)

#Problem 5-Modulo
def problem5():
    first_numberrr = int( input("Enter first number: ") )
    second_numberrr = int( input("Enter second number: ") )
    d = first_numberrr % second_numberrr
    return (d)

#Problem 6 -Volume of a cylinde
def problem6():
    pi = 3.141592
    r = float( input("Enter radius: ") )
    h = float( input("Enter height: ") )
    e = h * pi * r ** 2 
    return (e)

#Problem 7 -Perimeter of the square
def problem7():
    side = float( input("Enter one side: ") )
    f ="The perimeter of the square is "+ str( side * 4 )
    return (f)


   

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
