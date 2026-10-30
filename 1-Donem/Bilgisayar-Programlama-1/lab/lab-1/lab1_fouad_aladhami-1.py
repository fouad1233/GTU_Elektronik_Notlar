my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"

#Problem 1 -Indexing
def problem1():
    my_name = "Fouad"
    a = my_name[0]
    return (a)
    
#Problem 2 - Indexing II
def problem2():
    my_name = "Fouad"
    enterinput = int( input("Enter a number: ") )
    if enterinput > len(my_name) or enterinput < 0:
        enterinput == enterinput % ( len(my_name) + 1)
    b = my_name[enterinput]
    return (b)

#Problem 3 - Slicing
def problem3():
    my_name = "Fouad"
    first_number = int( input("Enter first number: ") )
    if first_number > len(my_name) or first_number < 0:
        first_number == first_number % ( len(my_name) + 1)
    second_number = int( input("Enter second number: ") )
    if second_number > len(my_name) or second_number < 0:
        second_number == second_number % ( len(my_name) + 1)
    c = my_name[min(first_number , second_number ) : max(first_number , second_number ) + 1]
    return (c)
#Problem 4-Vowels
def problem4():
    sentence = input("Enter input: ")
    bosluk = 0
    list2 = [" "]
    if sentence in list2:
        bosluk = bosluk + 1
    if (len(str(sentence)) - bosluk ) == 0:
        return 0
    elif (len(str(sentence)) - bosluk ) >= 0 and (len(str(sentence)) - bosluk ) <= 100 :
        count = 0
        list1= ["a" , "e" , "i" ,"o" , "u" ," A" , "E" , "I" , "O" , "U"]
        if sentence in list1:
            count = count + 1
    else:
        return
    return (count)
#Problem 5-Summation
def problem5():
    my_id = "210102002808"
    rakamtoplami = 0
    for rakam in str(my_id):
        rakamtoplami+= int(rakam)
    return (rakamtoplami)

#Problem 6 - Factorial
def problem6():
    number = int( input("Enter input: ") )
    carpim = 1
    if number > 0 and number <= 30:
        for i in range (1 , number):
            carpim = carpim*( i + 1 )
        return (carpim)
    elif number == 0:
        carpim == 1
        return (carpim)

#Problem 7 -Divisibility
def problem7():
    sayi = int( input("Enter a number: ") )
    if sayi%3 == 0 and sayi%7 == 0:
        return(True)
    else:
        return (False)
#Problem 8- Divisibility II
def problem8():
    numberr = int( input("Enter a number: ") )
    if numberr % 3 == 0 and numberr % 7 == 0:
        return(3)
    elif numberr % 3 == 0:
        return(1)
    elif numberr % 7 == 0:
        return(2)
#Problem 9- Prime Number 
def problem9():
    num = int( input("Enter a number: ") )
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return(False)
                break
            else:
                return(True)
#Problem 10- Square root[17 pts]
def problem10():
    number = abs(float(input("Enter a number: ")))
    guess = float("1")
    while number != guess**2 :
        guess = (1 / 2)*(guess + number / guess )
        if guess == (1 / 2)*(guess + number / guess ):
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
