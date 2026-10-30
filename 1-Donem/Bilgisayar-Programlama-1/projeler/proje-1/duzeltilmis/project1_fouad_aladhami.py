# -*- coding: utf-8 -*-
"""
Created on Sun Nov 14 10:42:47 2021

@author: sham tech
"""
"""

"""
"""
Versiyon 1.1 end on Tuesday Nov 9 10:15 2021
Versiyon 1.2
Merhaba bu ikinci versiyonda artik shuffle her zaman baska bir board veriyor.
ayni olup olmadigini kontrol etmek icin copylist adli fonksiyonu yaptim.
(.copy metodu ile yapmaya calisinca .copy ise yaramadi ve kopyaladigim board ,
 asil boardun degismesile o da degisiyordu ondan kendi copylist fonksiyonumu yapmaya karar verdim)
Okudugunuz icin tesekkurler


end on Sun Nov 14 01:13  2021 
"""

import random

my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"


def generate(row, column):
    #[[0, 1, 2], [3, 4, 5]].
    list1 = [ ]
    l = []
    
    for i in range(row * column):
        l = l + [i]
        a = l.copy()
        
        if (i + 1)% column == 0:
            list1.append(a)
            l.clear()
            
    return(list1)
def reset(board):
    
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    
    gnrte = generate(row, column)
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            board[c][i] = gnrte[c][i]
        c +=1
    return None
def is_solved(board):
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    if board == generate(row, column):
        return True
    else:
        return False
def get_board_size(board):
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    return (row ,column)
def print_board(board):
    c = 0
    for i in range(len(board)):
        print(end='\n')
        a = len(board[0])
        for i in range(a):
            print(board[c][i],end='\t')
        c +=1
    return None 
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
def is_valid(board):
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    
    e = []
    for i in range(0,row ):
        for j in range(0, column ):
            e = e + [ board[i][j] ]
    #print(e)
    for i in range(len(e)):
        #print(i)
        if e[i] > (row * column - 1):
            return False
        for j in range(i + 1, len(e)):
            #print(j)
            
            if e[i] == e[j]:
                return False
            
    return True
def move_right(board):
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and i >= a -1 :
                return 0
            elif board[c][i] == 0 and i < a :
                board[c][i] = board[c][i + 1]
                board[c][i + 1] = 0
                return 1
            
        c +=1
def move_left(board):
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and i == 0 :
                return 0
            elif board[c][i] == 0 :
                board[c][i] = board[c][i - 1]
                board[c][i - 1] = 0
                return 1
        c +=1
def move_up(board):
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and c == 0 :
                return 0
            elif board[c][i] == 0  :
                board[c][i] = board[c- 1][i ]
                board[c - 1][i ] = 0
                return 1
        c +=1   
def move_down(board):
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and c == len(board) - 1 :
                return 0
            elif board[c][i] == 0  :
                board[c][i] = board[c+ 1][i ]
                board[c + 1][i ] = 0
                return 1
        c +=1   
def play(board, moves):
    if is_valid(board) == False:
        return -2
    
    # if is_valid(board) == False :
    #     return -2
    # if board == is_solved(board):
    #     return 0
    
    i =0
    count = 0
    while  i <= len(moves):
        if board == is_solved(board):
            return 0
        if moves[i] == 'r' or moves[i] =='R':
            r = move_right(board)
            count += r
            i +=1
        elif moves[i] == 'l' or moves[i] =='L':
            count += move_left(board)
            i +=1
        elif  moves[i] == 'd' or moves[i] == 'D':
            count += move_down(board)
            i +=1   
        elif  moves[i] == 'u' or moves[i] == 'U':
            count += move_up(board)
            i +=1 
        else:
            i +=1
        if  is_solved(board) == True:
            
            return count
            break
        if i == len(moves)  :
            
            break
    if  is_solved(board) == False:
        return -1
def move(board, moves):
    i =0
    count = 0
    while  i <= len(moves):
        if moves[i] == 'r' or moves[i] =='R':
            r = move_right(board)
            count += r
            i +=1
        elif moves[i] == 'l' or moves[i] =='L':
            count += move_left(board)
            i +=1
        elif  moves[i] == 'd' or moves[i] == 'D':
            count += move_down(board)
            i +=1   
        elif  moves[i] == 'u' or moves[i] == 'U':
            count += move_up(board)
            i +=1 
        else:
            i +=1
        if i == len(moves)  :
            return count
            break         
def move_random(board):
    ablemovelist = []
    
    #Right side check code
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and i >= a -1 :
                continue
            elif board[c][i] == 0 and i < a :
                ablemovelist.append("R")
                break
        c +=1
    #LEFT SIDE CHECK CODE
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and i == 0 :
                continue
            elif board[c][i] == 0 :
                ablemovelist.append("L")
                break
        c +=1
    #UP side check code 
    c = 0
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and c == 0 :
                continue
            elif board[c][i] == 0  :
                ablemovelist.append("U")
                break
        c +=1   
    #DOWN side check code 
    c = 0
    
    for i in range(len(board)):
        a = len(board[0])
        for i in range(a):
            if board[c][i] == 0 and c == len(board) - 1 :
                continue
            elif board[c][i] == 0  :
                ablemovelist.append("D")
                break
        
        c +=1
    
    b = random.choice(ablemovelist)
    if  b =='R':
        move_right(board)
        
    elif b =='L':
        move_left(board)
        
    elif b == 'D':
        move_down(board)
           
    elif b == 'U':
        move_up(board)
    return b
def shuffle(board, times=20):
    checker = copylist(board)
    allmoves = ""
    #print("checker",checker)
    #print("board",board)
    for i in range(0,times):
        allmoves += move_random(board)
    #print("I am checker",checker)
    #print(board)
    while board == checker:
        allmoves = ""
        #print("checker",checker)
        print("board",board)
        for i in range(0,times):
            allmoves += move_random(board)
        #print("I am checker",checker)
        #print(board)
    return allmoves
def play_interactive(board=None):
    if board == None:
        print("Please type the puzzle size number.")
        row = int( input("Row number:") )
        column = int( input("Column number:") )
        board = generate(row, column)
        shuffle(board)
    totalmoves = ""
    
    if is_valid(board) == False:
        return ('', -2)
    while is_solved(board) == False:
        
        print("Current board is:")
        print_board(board)
        if is_solved(board) == True:
            print("Congrats! You solved the board in " , len(totalmoves) ," moves.")
            return(totalmoves , len(totalmoves) )
        move = str(input ("Where do you want to move: ") )
        if move == "R" or move == "r":
            r1 = move_right(board)
            if r1 == 1:
                totalmoves += "R"
        elif move == "L" or move == "l":
            l1 = move_left(board)
            if l1 == 1:
                totalmoves += "L"
        elif move == "U" or move == "u":
            U1 = move_up(board)
            if U1 == 1:
                totalmoves += "U"
        elif move == "D" or move == "d":
            D1 = move_down(board)
            if D1 == 1:
                totalmoves += "D"
        elif move == "M" or move == "m":
            yon = move_random(board)
            totalmoves += yon
        elif move == "Q" or move == "q":
            print("Exiting.")
            if is_solved(board) == True:
                return(totalmoves , len(totalmoves) )
            elif is_solved(board) == False:
                return(totalmoves , -1 )
        else:
            print("Wrong move.")
    if is_solved(board) == True:
            print("Congrats! You solved the board in " , len(totalmoves) ," moves.")
            return(totalmoves , len(totalmoves) )    
    
def copylist(board):
    c = 0
    yeniliste = []
    for i in range(len(board)):
        yeniliste.append([])
        
        a = len(board[0])
        for i in range(a):
            yeniliste[c].append(board[c][i])
        c +=1
    return yeniliste











    



if __name__ == "__main__":
    print(f"My name is {my_name}.")
    print(f"My number is {my_id}.")
    print(f"My email is {my_email}.")
    
    