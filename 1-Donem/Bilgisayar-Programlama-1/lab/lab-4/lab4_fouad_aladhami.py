# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:36:05 2021

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
#Problem 1 - Pick [4 pts]
def problem1( x , y):
    if y > ( len(x) - 1 ) or y < 0:
        return None
    else:
        return x[y]
    
    
    
#Problem 2 - Remove [4 pts]
def problem2( list1 , z):
    
    
    if z > ( len(list1) - 1 ) or z < 0 or len(list1) == []:
        return list1
    else:
        a = list1[z]
        list1.remove(a)
        return list1
#Problem 3 - Sort [5 pts]
def problem3( l , des ):
    if des == True:
        l.sort()
        return l
    elif des == False :
        l.sort()
        l.reverse()
        return l
#Problem 4 - Common Numbers [8 pts]
def problem4( l1 , l2 ):
    count = 0
    for i in l1 :
        if i in l1 and i in l2:
            
            for i in l2:
                count = count + 1
                while i in l2:
            
                    l2.remove(i)
    return count
#Problem 5 - Weighted Average [8 pts]
def problem5( l , w ):
    s = []
    a = 0
    wtop = 0
    for i in range(0,len(w)):
        s.append( (l[i]*w[i]) )
    for i in range(0,len(s)):
        a += s[i]
    for i in range(0,len(w)):
        wtop += w[i]    
    b = a / wtop
    
    return b
#Problem 6 - Determinant [10 pts]
def problem6(x):
    z = 0 
    if len(x[0]) == 2 and len(x[0]) == len(x[1]) :
        z = x[0][0] * x[1][1] - x[0][1] * x[1][0]
        return float(z)
    
    elif len(x[0]) == 3 and len(x[0]) == len(x[1]) == len(x[2]) and len(x) == 3:
        a = x[0][0]
        b = x[0][1]
        c = x[0][2]
        
        d = x[1][0]
        e = x[1][1]
        f = x[1][2]
        
        g = x[2][0]
        h = x[2][1]
        i = x[2][2]
        
        z = a * problem6([[e , f] , [ h , i]]) - b * problem6([[a , f] , [ g , i]]) + c * problem6([[d , e] , [ g , h]])
        return float(z)
    elif len(x[0]) == 1 and len(x) == 1:
        return float(x[0][0])
    elif len(x[0]) == 4 and len(x[0]) == len(x[1]) == len(x[2]) == len(x[3]) and len(x) == 4:
        a = x[0][0]
        b = x[0][1]
        c = x[0][2]
        d = x[0][3]
        
        e = x[1][0]
        f = x[1][1]
        g = x[1][2]
        h = x[1][3]
        
        i = x[2][0]
        j = x[2][1]
        k = x[2][2]
        l = x[2][3]
        
        m = x[3][0]
        n = x[3][1]
        o = x[3][2]
        p = x[3][3]
        
        z = a * problem6([ [f,g,h],[j,k,l],[n,o,p] ]) - b * problem6([ [e,g,h],[i,k,l],[m,o,p] ]) + c * problem6([ [e,f,h],[i,j,l],[m,n,p] ]) - d * problem6([ [e,f,g],[i,j,k],[m,n,o] ])
        return float(z)
    else:
        return None
#Problem 7 - Withdraw [18 pts]
def problem7(accounts, source, lira ,kurus):
    if source < 0 or source > len(accounts) -1:
        return accounts
    else:
        
        accountskurus = accounts[source][:-3:-1]
        accountskurus = accountskurus[::-1]
        accountslira = accounts[source][-4::-1]
        accountslira = accountslira[::-1]
        liratoplami = int(accountslira) - int(lira)
        kurustoplami = int(accountskurus) - int(kurus)
        if kurustoplami  < 0:
            kurustoplami = 100 + kurustoplami 
            liratoplami = liratoplami - 1
        if kurustoplami > 0 and kurustoplami < 10:
            kurustoplami = "0" + str(kurustoplami)
        kalanpara = str(liratoplami) + "." + str(kurustoplami)
        
        
        if float(kalanpara) >= 0:
            accounts[source] = kalanpara
            return accounts
        else:
            return accounts
#Problem 8 - Transfer [22 pts]
def problem8(accounts, source, destination, lira, kurus,fee = False):
    if source < 0 or source > len(accounts) -1 or destination < 0 or destination > len(accounts) -1 or destination == source :
        return accounts
    else:
        accountskurus = accounts[source][:-3:-1]
        accountskurus = accountskurus[::-1]
        accountslira = accounts[source][-4::-1]
        accountslira = accountslira[::-1]
        destinationkurus = accounts[destination][:-3:-1]
        destinationkurus = destinationkurus[::-1]
        destinationlira = accounts[destination][-4::-1]
        destinationlira = destinationlira[::-1]
        liratoplami = int(accountslira) - int(lira)
        kurustoplami = int(accountskurus) - int(kurus)
        transeferdensonratoplampara = str(int(destinationlira) +int( lira)) +"."+ str(int(destinationkurus) + int( kurus) )
        transucreti = 0
        transucretikurus = 0
        transucretilira = 0
        transedilenpara = float(str(lira) + "." + str(kurus ) )
        if fee == True and transedilenpara < 10:
            transucretikurus = 10
        elif fee == True and transedilenpara > 10:
            transucreti = transedilenpara / 100
            transucretikurus =  transucreti - int(transucreti) 
            transucretikurus = str(transucretikurus)[:4:1]
            transucretikurus = transucretikurus[:-3:-1]
            transucretikurus = transucretikurus[::-1]
            transucretilira = int(transucreti)
        if kurustoplami  < 0:
            kurustoplami = 100 + kurustoplami 
            liratoplami = liratoplami - 1
        sonkalankurus = int(kurustoplami) - int ( transucretikurus )
        if sonkalankurus > 0 and sonkalankurus < 10:
            sonkalankurus = "0" + str(sonkalankurus)
        kalanpara = str(int(liratoplami) - int(transucretilira) ) + "." + str(sonkalankurus) 
        
        
        
        if float(kalanpara) >= 0:
            accounts[source] = kalanpara
            accounts[destination] = transeferdensonratoplampara
            return accounts
        else:
            return accounts
#Problem 9 - Bom 7 [13 pts]  
#Problem 9 - Bom 7 [13 pts]  
def problem9(x):
    x = list(range(x + 1))
    x.pop(0)
    #print(x)
    count = 0
    c = 0
    a = []
    while len(x) != 1:
        
        a += [x[count] ,]
        #print(a)
        c += 1
        #print(c,"ccccccccccccccc")
        #print(count,"countttttttttt")
        if len(x) == 1:
            break
        if c % 7 == 0:
            a.clear()
            c =0 
            x.pop(count  )
            count = count - 1
            #print(x)
            
        count += 1
        if len(x) == 1:
            break
        
        
        
        if count%( len(x)  ) == 0:
            count = 0
            
    return x[0]
        
    
         
         
         
        
     
def problem10(x):
    if len(x) == 1 or len(x) == 0:
        return None
    if x[-1] == x[0]:
        
        return x[0]
    for i in range( 0 ,len(x) -1 ):
        for j in range( i + 1 ,len(x) -1 ):
            if x[i] == x[j]:
                return x[i]
    
    return None
    
    
   

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
    print( problem1([1, 2, 3], 2) )
    print( problem1([1, 2, 3], -1) )
    print( problem1([1, 2, 3], 4) )
    
    print("Running problem 2")
    print( problem2([], 2) )
    print( problem2([1, 2, 3], 2) )
    print( problem2([1, 2, 3], -1) )
    print(problem2([1, 2, 3], 4) )
    
    print("Running problem 3")
    print( problem3([2, 1, 3], False) )
    print( problem3([2, 1, 3], True) )
    

    print("Running problem 4")
    print( problem4([1, 2, 3], [1, 3, 2]) )
    print( problem4([1, 2, 3], [2, 2, 2]) )
    print( problem4([1, 2, 3], [4, 5, 6]) )
    print( problem4([1, 2, 3], [3]) )
    print( problem4([1, 2, 3], []) )
    print( problem4([1], [3, 5, 2]) )
    print( problem4([], [3, 5, 2]))
    
    print("Running problem 5")
    print(problem5([1, 2, 3], [0.1, 0.2, 0.3]))
    print( problem5([1, 2, 3], [.5, .5, .5]) )
    
    print("Running problem 6")
    print(problem6([[3, 7], [1, -4]]))
    print(problem6([[1]]))
    print(problem6([[3, 7], [1, 2, 3]]))
    print( problem6([ [6 , 1 , 1], [ 4 , -2 , 5] , [2 , 8 , 7] ] ) )
    print( problem6([ [4 , 3 , 2 , 2], [ 0 , -1 , -3 , 3] , [0 , -1 , 3 , 3],[0 , 3 , 1 , 1]  ] ) )
    
    
    
    print("Running problem 7")
    print(problem7(accounts=["11.23", "10.43", "100.63", "0.10"], source=-1, lira=10,kurus=13) )
    print( problem7(["11.23", "10.43", "100.63", "0.10"], 1, 10, 41) )
    print(problem7(["11.23", "10.43", "100.63", "0.10"], 4, 10, 13))
    print(problem7(["11.23", "10.43", "100.63", "0.10"], 3, 10, 13))
    
    print("Running problem 8")
    print( problem8(accounts=["11.23", "10.43", "100.63", "0.10"], source=0,destination=1, lira=11, kurus=23) )
    print( problem8(accounts=["11.23", "10.43", "100.63", "0.10"], source=0,destination=0, lira=10, kurus=13) )
    print(problem8(accounts=["11.23", "10.43", "100.63", "0.10"], source=3,destination=0, lira=10, kurus=13))
    print(problem8(accounts=["11.23", "10.43", "100.63", "0.10"], source=0,destination=1, lira=9, kurus=13, fee=True))
    print(problem8(accounts=["11.23", "10.43", "100.63", "0.10"], source=0,destination=1, lira=10, kurus=13, fee=True))
    
    
    print("Running problem 9")
    print( problem9(5) )
    print("Running problem 10")
    print( problem10(['1', '25', '36', '4', '1', '5']) )
    print(problem10(['a','s','blasdf','dx','c','x','z','1','c','5']))
    print(problem10(['aba', 'hede', '1', 'aba']))
    print(problem10([problem10(['aba'])]))
    print(problem10(['aba']) )
    