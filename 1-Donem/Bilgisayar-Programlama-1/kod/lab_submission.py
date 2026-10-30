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

my_name = "Furkan Cayci"
my_id = "12345678"
my_email = "furkancayci@gtu.edu.tr"

def problem0():
    # This problem is just an example and will not be graded
    # You can delete this function after reviewing it.
    # everything that belongs to problem0 has the same indentation level (or deeper if needed)
    # variable names can be anything except some keywords that the language itself use, like def, return, if, for, etc.
    var1 = 4
    var2 = var1 * 2
    var3 = int( input("Enter a number") )
    var4 = var2 * var3
    # printing messages will not be graded and will be ignored.
    print(var4)
    # Don't forget to return, printing will not give you any grade
    return var4

def problem1():
    # Write problem 1 code here
    # remove pass
    pass

def problem2():
    # Write problem 2 code here
    # remove pass
    pass

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
