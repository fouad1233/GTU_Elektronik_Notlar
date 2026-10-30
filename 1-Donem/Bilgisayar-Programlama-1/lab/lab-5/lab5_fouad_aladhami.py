# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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

def problem1(x , y):
    """
    

    Problem 1 -nth frequency [5 pts]
    Write a function that takes two arguments; 
    a list and an integer called n.
    Return the list of numbers that repeats n times
    .●Function parameter names do not matter, 
    but the function shouldexpect 2parameters.
    ●inputs :○l = { x : x is list and len(x)∈[0:200]}and li∈ℤ○n∈ℤ
    ●output : list
    >>> problem1([1, 2, 1, 1, 1, 2, 3, 4], 1)
    [3, 4]
    >>> problem1([1, 2, 1, 1, 1, 2, 3, 4], 0)
    []
    >>> problem1([1, 2, 1, 1, 1, 2, 3, 4], -2)
    []
    >>> problem1([1, 2, 1, 1, 1, 2, 3, 4], 2)
    [2]
    >>> problem1([1, 2, 1, 1, 1, 2, 3, 4], 3)
    []
    >>> problem1([], 0)
    []
    >>> problem1([], 1)
    []

    """
    
    a = []
    d = []
    # if y == 0 :
    #     return []
    b = len(x)
    for i in range(b):
        
        count = 1
        for j in range(i + 1 , b):
            
            if x[i] == x[j]:
                count += 1
        
        
            
        if x[i] not in d :
            if count == y:
                a.append(x[i])
        
        d.append(x[i])
        
    return a
        
    
    

def problem2(x):
    """
    Problem 2 -Median grade [7 pts]
    Write a function that takes one argument: a dictionary.
    It will have the name, gradepair for the INF211 class.
    Find and return the median grade of the class.
    ●If the number of people is odd, return the middle grade.
    ●If the number of people is even, take the mean (average) of the two middlemost numbers and return that.
    ●if the dictionary isempty, return 0.
    ●Function parameter names do not matter.
    ●input : l = { x : x is dict and len(x)∈[0:1000]}
    ●output : integer or float
    >>> problem2({'ahmet': 30, 'ali': 20, 'mehmet':10})
    20
    >>> problem2({'ahmet': 10, 'ali': 20})
    15

    """
    a = list(x.values())
    a.sort()
    if len(a)%2 == 1:
        return  a[ ((len(a)+1)/2 )-1] 
    if len(a)%2 == 0:
        return ( a[ (len(a))/2 - 1] + a[ (len(a))/2] ) / 2
def problem3(x):
    # '''
    # Problem 3 - Read Transcript [13 pts]
    # Write a function that takes a filename as parameter. File will have a list of courses with the credits , given term and the scores. You need to read this file, create a dictionary for each course and add it to a list. Finally return this list. Example file is given with the assignment.
    # ● Function parameter names do not matter.
    # ● Dictionary keys will be: name, credit, term, and grade.
    # ● If the given course does not have a grade, enter NA.
    # ○ There will be a comma at the end for sure. Check the example txt file.
    # ● File will only have '\n' for the newline.
    # ● File will use a comma as a separator between items.
    # ● File will have name, credit, term, grade in that order.
    # ● If the file is empty, return an empty list.
    # ● If the file cannot be read or not found or not properly parsed, return an empty list.
    # ● input : f = filename as string
    # ● output : list
    # >>> problem3('transcript1.txt')
    # [{'name' : 'inf211', 'credit' : 6, 'term' : 1, 'grade' : 'DC'},
    #  {'name' : 'elm101', 'credit' : 2, 'term' : 1, 'grade' : 'BA'},
    #  {'name' : 'mat101', 'credit' : 7, 'term' : 1, 'grade' : 'BB'}]
    # >>> problem3('transcript2.txt')
    # [{'name' : 'inf211', 'credit' : 6, 'term' : 1, 'grade' : 'DC'},
    #  {'name' : 'elm101', 'credit' : 2, 'term' : 1, 'grade' : 'BA'},
    #  {'name' : 'mat101', 'credit' : 7, 'term' : 1, 'grade' : 'BB'},
    #  {'name' : 'inf212', 'credit' : 6, 'term' : 2, 'grade' : 'NA'}]
    # >>> problem3('transcript_empty.txt')
    # []
    # >>> problem3('some_random_filename_that_does_not_exist.txt')
    # []
    

    # '''
    # the check fonction check if the file can be opened ,and if its empty or not
    if check(x) == False:
        return []

    l1 = ["name", "credit", "term", "grade"]
    f = open(x , "r")
    
    a = f.read()
    a = a.split('\n')
    new = []
    list_dict = []
    
    for row in a:
        new.append(row.strip().split('\t'))
    
    #print(new)
    for i in range (len(new) - 1):
        l2 = new[i][0].split(",")
        
        
        list_dict.append( dict(zip(l1,l2)) )
    for j in range(len(list_dict)):
        if list_dict[j]['grade'] =='':
            list_dict[j]['grade'] = ' NA'
    
    for c in range(len(list_dict)):
            list_dict[c]['credit'] = int(list_dict[c]['credit'])
            list_dict[c]['term'] = int(list_dict[c]['term'])
    for b in range(len(list_dict)):
        list_dict[b]['grade'] = list_dict[b]['grade'][1:]
    f.close()    
    return list_dict
def check(x) :
    try:
        with open(x) as f:
            return True
            # Do something with the file
    except IOError:
        return False

def problem4(dic , tnum):
    """
    
    Problem 4 - Term GPA [14 pts]
    Write a function that takes two parameters: a list that holds the transcript as dictionary items (as given in the problem 3), and a term number. You need to calculate the GPA for a given term and return the term GPA.
    ● Function parameter names do not matter.
    2
    INF 211 - Algorithms and Programming I - Electronics Engineering - Gebze Technical University - Fall 2021
    ● If any of the courses in the given term does not have a grade, do not take that into calculation.
    ● If the dictionary is empty, or the term does not have any courses, return 0.
    ● Each grade corresponds to a number:
    ○ AA-4.0,BA-3.5,BB-3.0,CB-2.5,CC-2.0,DC-1.5,DD- 1.0, FF - 0.0, NA - NA
    ○ Note that FF will be taken into consideration but NA will not be taken into consideration.
    ● GPA calculation is done using weighted average.
    ● input :
    ○ d = list of dictionaries ○ t={x:x ∈ [1:8]}
    ● output : float
    >>> problem4([{'name' : 'inf211', 'credit' : 6, 'term' : 1, 'grade' : 'DC'},{'name' : 'elm101', 'credit' : 2, 'term' : 1, 'grade' : 'BA'},{'name' : 'mat101', 'credit' : 7, 'term' : 1, 'grade' : 'BB'}], 1)
    2.466666666666667
    >>> problem4([{'name' : 'inf211', 'credit' : 6, 'term' : 1, 'grade' : 'DC'},{'name' : 'elm101', 'credit' : 2, 'term' : 1, 'grade' : 'BA'},{'name' : 'mat101', 'credit' : 7, 'term' : 1, 'grade' : 'NA'}], 1)
    2.0
    >>> problem4([{'name' : 'inf211', 'credit' : 6, 'term' : 1, 'grade' : 'DC'},{'name' : 'elm101', 'credit' : 2, 'term' : 1, 'grade' : 'BA'},{'name' : 'mat101', 'credit' : 7, 'term' : 1, 'grade' : 'FF'}], 1)
    1.0666666666666667
    >>> problem4([{'name' : 'inf211', 'credit' : 6, 'term' : 1, 'grade' : 'DC'},{'name' : 'elm101', 'credit' : 2, 'term' : 1, 'grade' : 'BA'},{'name' : 'mat101', 'credit' : 7, 'term' : 1, 'grade' : 'BB'}], 2)
    0
    >>> problem4([], 1)
    0

    """
    toplam = 0
    credit = 0
    a = {'AA' : 4.0 , 'BA' : 3.5 , 'BB' : 3.0 , 'CB' :2.5 ,'CC' : 2.0, 'DC': 1.5,'DD' : 1.0, 'FF' : 0.0}
    for i in range(len(dic)):
        if dic[i]['term'] == tnum and dic[i]['grade'] in a:
            toplam +=  (a[dic[i]['grade']] * dic[i]['credit']) 
            credit += dic[i]['credit']
    if toplam== 0 and credit == 0:
        return 0
    waverage = toplam / credit
    return int(waverage*100) / 100
def ffunc(x):
    top = 0
    for i in range(x + 1):
        for j in range(len(str(i))):
            
            if "1" in str(i)[j]:
                top += 1
    return top       
        
def problem5(func , num):
    if func(num) == ffunc(num):
        return True
    else:
        return False
    
def product(*args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [tuple(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)
    

def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    for indices in product(range(n), repeat=r):
        if len(set(indices)) == r:
            yield tuple(pool[i] for i in indices)

def problem6(x):
    '''
    Problem 6 - Combinations [10 pts]
    Write a program that accepts a string and returns all possible combinations of the given strings.
    ● There should not be any duplicates in the returned list.
    ● The list should be ordered.
    ● Returned list should be lowercase.
    ● The words do not need to have a meaning.
    ● inputs : s = { x : x is English letters and len(x) ∈ [1:10]}
    ● outputs: list of strings
    >>> problem6("a")
    ['a']
    >>> problem6("AB")
    ['a', 'ab', 'b', 'ba']
    >>> problem6("aba")
    ['a', 'aa', 'aab', 'ab', 'aba', 'b', 'ba', 'baa']

    '''
    if len(x) == 0:
        return [] #if the given  list is empty
    x = x.lower()
    c = []
    x = sorted(x) 
    for i in x:
        c.append(i)
        #print(c)
    d = []
    for i in range(len(c)):
        permut = permutations(c,i+1)
        #print(list(permut))
        for j in list(permut):
            d.append(''.join(j))
    d = list(dict.fromkeys(d))
    finallist = sorted(d)
    return finallist
    '''
    


    >>> problem6("a")
    ['a']
    >>> problem6("AB")
    ['a', 'ab', 'b', 'ba']
    >>> problem6("aba")
    ['a', 'aa', 'aab', 'ab', 'aba', 'b', 'ba', 'baa']
    '''
    
    # x = x.lower()
    # y = sorted(x)
    # z = permutations(y, len(y))
    # # for i in range(len(y)):
    # #     z += y[i]
    # return z
    # colist= []
def problem7(string,doc):
    '''
    

    Problem 7 - Anagrams [5 pts]
    Write a function that takes two parameters. First parameter is a string of arbitrary length, and the
    second parameter is a filename for a file that holds valid words. Write the function so that it should 4
    INF 211 - Algorithms and Programming I - Electronics Engineering - Gebze Technical University - Fall 2021
    find all possible combinations of this string that are included in the given words list. Return the valid words, all lowercase and sorted, as a list.
    ● Function parameter names do not matter.
    ● For testing words, you can generate your own, or you can download [1].
    ● If no words are found, return an empty list.
    ● if an empty string is given, return an empty list.
    ● inputs :
    ○ s:s={x:xisEnglishlettersandlen(x) ∈ [1:10]}
    ○ f : filename
    ● output : list of strings
    >>> problem7("abaa", "words.txt")
    ['a', 'aa', 'aaa', 'ab', 'aba', 'b', 'ba', 'baa']
    >>> problem7("ABAA", "words.txt")
    ['a', 'aa', 'aaa', 'ab', 'aba', 'b', 'ba', 'baa']

    '''
    f = open(doc , "r")
    
    a = f.read()
    a = a.split('\n')
    f.close()
    mylist = problem6(string)
    copylist = mylist.copy()
    for i in range(len(mylist)) :
        if copylist[i] not in a:
            mylist.remove(copylist[i])
    return mylist
def get_board_size(board):
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    return (row ,column)
def rotate(board):
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    b = []
    c = []
    for i in range(0,column ):
        for j in range(0, row):
            c = c + [ board[j][i] ]
            d = c.copy()
            if (j + 1)% row == 0:
                b.append(d)
                c.clear()
    return b
def problem8(matrix,sub):
    '''
    
    Problem 8 - Sub-matrix [14 pts]
    Write a function that will take two parameters, both are list of lists representing a matrix. The function should find and return True if the second matrix is a sub-matrix of the first one. If it is not a sub-matrix, return False.
    ● Function parameter names do not matter.
    ● For example, for an m matrix given as :
    123 456 789
    Some of the valid sub-matrices (n) are given as:
    123 123 21123 12 156 456 5456454 78987
    ● inputs :
    ○ m = { x : x is list } and mi = { x : x is list } and len(m) ∈
    [1:10] and len(mi) ∈ [1:10] and mij ∈ Z
    ○ n = { x : x is list } and ni = { x : x is list } and len(n) ∈
    [1:10] and len(mi) ∈ [1:10] and nij ∈ Z
    ● output : Boolean
    >>> problem8([[1, 2], [3, 4]], [[1]])
    True
    >>> problem8([[1, 2], [3, 4]], [[5]])
    False
    >>> problem8([[1, 2], [3, 4]], [[1, 2], [3, 4]])
    True
    >>> problem8([[1, 2], [3, 4]], [[1, 3]])
    False
    >>> problem8([[1, 2], [3, 4]], [[1], [3]])
    True
    >>> problem8([[1, 2], [3, 4]], [[1, 2, 3], [3, 4, 5]])
    False

    '''
    a , b = get_board_size(matrix)# a is row b is coulumn of the matrix
    c , d = get_board_size(sub)
    if matrix == sub:
        return True
    if c > a or d > b:
        return False
    if c == 1 and d == 1:
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                if matrix[i][j] == sub[0][0]:
                    return True
                elif i + 1 == a and j + 1== b:
                    return False
    def finder():
        if c > 1 or d > 1:
            for i in range(a):
                for j in range(b):
                    if matrix[i][j] == sub[0][0]:
                        return i,j
    x,y = finder() #x is row and y is coulumn of the first index of sub
    
    o = 0
    p = 0
    while x < a :
        if matrix[x][y] != sub[o][p]:
            return False
        y += 1
        p += 1
        if p == d:
            p = 0
            bla,y = finder()
            x += 1
            o += 1
    return True
        
        # bu kodlar problem 8 i yapmamın 3 üncü başarısız 
        #denememden  kaldı . Hatıra olarak kalsın :-)
        # def checkrow():
        #     for i in range(c):
        #         for h in range(d):
                    
        #             for j in range(a):
        #                 for k in range (b):
        #                     if sub[i][h] != matrix[j][k]:
        #                         return False
        # def checkcolumn ():
        #     rotated_sub = rotate(sub)
        #     rotated_matrix = rotate(matrix)
        #     a , b = get_board_size(rotated_matrix)# a is row b is coulumn of the matrix
        #     c , d = get_board_size(rotated_sub)
            
        #     for i in range(c):
        #         for j in range(a):
        #             if rotated_sub[i] not in rotated_matrix[j]:
        #                 return False
        # if checkrow() == False and checkcolumn() ==False:
        #     return False
        # return True
    
    
    
def problem9(string):
    '''
    
    Problem 9 - Compression [7 pts]
    Our engineers developed a novel compression algorithm that they claim will save a lot of space when saving text files. In this algorithm, if a letter is consequently repeated more than 1 time, instead of writing the letter multiple times, a number is appended to denote how many times the preceding letter is repeated. Write a program that compresses the given string, and returns the compressed version as a string and the compression rate as a percentage rounded to an integer.
    ● Function parameter names do not matter.
    ● Compression rate is described as the percentage of saved space.
    ● If the letter happens only 1 time, no number should be appended.
    ● inputs : s = { x : x is English letters and len(x) ∈ [0:1000]}
    ● outputs: a tuple of (string, integer)
    >>> problem9('gol')
    ('gol', 0)
    >>> problem9('gollllllll')
    ('gol8', 60)
    >>> problem9('ggoooooooooooolllllllllllll')
    ('g2o12l13', 70)
    >>> problem9('ggoooooooooooollllllllllllll')
    ('g2o12l14', 71)

    '''
    newstr = ""
    count = 1
    counter = 0
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            if count == 1:
                newstr += string[i ]
                counter += 1
            count += 1
            if i == len(string) - 2:
                newstr += str(count)
                
                count = 1
            
        else:
            
            if count != 1:
                newstr += str(count)
                
                count = 1
            else:
                newstr += string[i ]
                counter += 1
            if i == (len(string) - 2) and count == 1:
                newstr += string[i + 1 ]
                
    pourcentage = 100 - (len(newstr) / len(string)) *100
    
    return newstr , round(pourcentage)

def problem10(x):
    '''
    

    >>> problem10([1, 3, 2, 5])
    4
    >>> problem10([4, 1, 2])
    3
    >>> problem10([0, -1, -2, 2, 3])
    1
    >>> problem10([0])
    1
    >>> problem10([5, 3, 4])
    6

    '''
    x.sort()
    for i in range (len(x) -1):
        if (x[i] + 1) != x[i + 1]:
            return x[i] + 1
    return x[-1] + 1

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
    import doctest
    doctest.testmod()
    

