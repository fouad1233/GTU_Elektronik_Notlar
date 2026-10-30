#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 20:26:31 2021

@author: fuad
"""
import random
def generate_random(row, column):
    l1 = ['red','green','blue']
    
    l4 = []
    for j in range (row):
        l3 = []
        for i in range(column):
            l2 = [random.randint(0,255) , random.randint(0,255) , random.randint(0,255)]
            l3.append( dict(zip(l1,l2)) )
        
        l4.append(l3)
    
    return l4
def get_board_size(board):
    row = len(board)
    if len(board) > 0:
        column = len(board[0])
    else:
        column = 0
    return (row ,column)
def clear(img):
    row , column = get_board_size(img)
    for i in range(row):
        for j in range(column):
            img[i][j]['red'] = 0
            img[i][j]['green'] = 0
            img[i][j]['blue'] = 0
    return None

def is_valid(img):
    row , column = get_board_size(img)
    for i in range(row):
        for j in range(column):
            if img[i][j]['red'] < 0 or img[i][j]['red'] > 255 or type(img[i][j]['red']) != type(1) :
                return False
            if img[i][j]['green'] < 0 or img[i][j]['green'] > 255 or type(img[i][j]['green']) != type(1):
                return False
            if img[i][j]['blue'] < 0 or img[i][j]['blue'] > 255 or type(img[i][j]['blue']) != type(1):
                return False
            
    return True

def rotate90(board):
    A = copylist(board)
    N = len(board[0][0])
    for i in range(N // 2):
        for j in range(i, N - i - 1):
            temp = A[i][j]
            A[i][j] = A[N - 1 - j][i]
            A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
            A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
            A[j][N - 1 - i] = temp
    fix(A)
    return  A
def rotate180(board):
    a = rotate90(board)
    b = rotate90(a)
    fix(b)
    return b
def rotate270(board):
    a = rotate180(board)
    b = rotate90(a)
    fix(b)
    return b
def copylist(board):
    l1 = ['red','green','blue']
    c = 0
    l2 = []
    yeniliste = []
    for c in range(len(board)):
        l3 = []
        yeniliste.append(l3)
        a = len(board[0])
        for i in range(a):
            l2.clear()
            l2.append(board[c][i]['red'])
            l2.append(board[c][i]['green'])
            l2.append(board[c][i]['blue'])
            
            l3.append( dict(zip(l1,l2)) )
        c +=1
    return yeniliste
#board = [[{'red': 137, 'green': 42, 'blue': 178}, {'red': 28, 'green': 50, 'blue': 124}]]
# def mirror_x(img):
#     row , column = get_board_size(img)
#     a = copylist(img)
#     c = 0
#     d = 0
#     o = row
#     for i in range(row):
#         o -= 1
#         for j in range(column ):
#             img[c][j]['red'] = a[o][d]['red']
#             img[c][j]['green'] = a[o][d]['green']
#             img[c][j]['blue'] = a[o][d]['blue']
#             d += 1
#         c += 1 
#     return None
# mirror_x(board)
def read_from_file(filename):
    f = open(filename , "r")
    
    a = f.read()
    a = a.strip().split('\n')
    new = []
    # list_dict = []
    l3 = []
    for row in a:
        new.append(row.strip().split('\t'))
    
    #print(new)
    for i in range (len(new) ):
        l2 = new[i][0].strip().split(",")
        l3.append(l2)
    
    row , column = get_board_size(l3)
    # return l3
    for i in range(row):
        for j in range(column):
            b = hextorgb(l3[i][j])
            l3[i][j] = b[0]
    #print(l3)
    f.close()
    fix(l3)
    return l3
def hextorgb(h):
    
    h.lstrip('#')
    l3 = []
    l1 = ['red','green','blue']
    a =( list(int(h[i:i+2], 16) for i in (0, 2, 4)))
    l3.append( dict(zip(l1,a)) )
    return l3
def rgbtohex(h):
    return '%02x%02x%02x' % tuple(h.values())

    
def write_to_file(img, filename):
    
    b = []
    
    row , column = get_board_size(img)
    for i in range(row):
        a = []
        for j in range(column):
            a.append( rgbtohex(img[i][j] ) )
        b.append(a)
    #print(l3)
    f = open(filename, "w")
    f.write(str(b))
    f.close()

    
    return None

def set_value(img, value, channel='rgb'):
    row , column = get_board_size(img)
    for d in range(len(channel)):
        if channel[d] == 'r':
            for i in range(row):
                for j in range(column):
                    img[i][j]['red'] = value
            
        if channel[d] == 'g':
            for i in range(row):
                for j in range(column):
                    img[i][j]['green'] = value
        if channel[d] == 'b':
            for i in range(row):
                for j in range(column):
                    img[i][j]['blue'] = value
    fix(img)
    return None

def fix(img):
    row , column = get_board_size(img)
    for i in range(row):
        for j in range(column):
            #red channel fixer
            if img[i][j]['red'] > 255:
               img[i][j]['red'] = 255 
            if img[i][j]['red'] < 0:
               img[i][j]['red'] = 0
            if type(img[i][j]['red']) != type(1) :
               img[i][j]['red'] = round(img[i][j]['red'])
            #green channel fixer
            if img[i][j]['green'] > 255:
               img[i][j]['green'] = 255 
            if img[i][j]['green'] < 0:
               img[i][j]['green'] = 0
            if type(img[i][j]['green']) != type(1) :
               img[i][j]['green'] = round(img[i][j]['green'])
            # blue channel fixer
            if img[i][j]['blue'] > 255:
               img[i][j]['blue'] = 255 
            if img[i][j]['blue'] < 0:
               img[i][j]['blue'] = 0
            if type(img[i][j]['blue']) != type(1) :
               img[i][j]['blue'] = round(img[i][j]['blue'])
    return None
def mirror_y(img):
    row , column = get_board_size(img)
    a = copylist(img)  
    
    for i in range(row):
        for j in range(column):
            img[i][j]['red'] = a[row - i -1][j]['red']
        
            img[i][j]['green'] = a[row - i -1][j]['green']
    
            img[i][j]['blue'] = a[row - i -1][j]['blue']
    fix(img)
    return None
    
def mirror_x(img):
    row , column = get_board_size(img)
    a = copylist(img)  
    
    for i in range(row):
        for j in range(column):
            img[i][j]['red'] = a[i][column - j -1]['red']
        
            img[i][j]['green'] = a[i][column - j -1]['green']
    
            img[i][j]['blue'] = a[i][column - j -1]['blue']
    fix(img)
    return None
    
def enhance(img, value, channel='rgb'):
    row , column = get_board_size(img)
    for d in range(len(channel)):
        if channel[d] == 'r':
            for i in range(row):
                for j in range(column):
                    img[i][j]['red'] = round(value*img[i][j]['red'])
            
        if channel[d] == 'g':
            for i in range(row):
                for j in range(column):
                    img[i][j]['green'] = round(value*img[i][j]['green'])
        if channel[d] == 'b':
            for i in range(row):
                for j in range(column):
                    img[i][j]['blue'] = round(value*img[i][j]['blue'])
    fix(img)                
    return None
def grayscale(img, mode=1):
    row , column = get_board_size(img)
    a = copylist(img)
    if mode == 1 :
        for i in range(row):
            for j in range(column):
                img[i][j]['red'] = round(a[i][j]['red'] + a[i][j]['green'] + img[i][j]['blue'] ) / 3
                img[i][j]['green'] = round(a[i][j]['red'] + a[i][j]['green'] + img[i][j]['blue'] ) / 3
                img[i][j]['blue'] = round(a[i][j]['red'] + a[i][j]['green'] + img[i][j]['blue'] ) / 3
    if mode == 2:
        for i in range(row):
            for j in range(column):
                img[i][j]['red'] = round(a[i][j]['red'] * 0.299 + a[i][j]['green']*0.587 + img[i][j]['blue']*0.114 )
                img[i][j]['green'] = round(a[i][j]['red'] * 0.299 + a[i][j]['green']*0.587 + img[i][j]['blue']*0.114 )
                img[i][j]['blue'] = round(a[i][j]['red'] * 0.299 + a[i][j]['green']*0.587 + img[i][j]['blue']*0.114 )
        
        
    if mode == 3:
        for i in range(row):
            for j in range(column):
                img[i][j]['red'] = round(a[i][j]['red'] * 0.2126 + a[i][j]['green']*0.7152 + img[i][j]['blue']*0.0722 )
                img[i][j]['green'] = round(a[i][j]['red'] * 0.2126 + a[i][j]['green']*0.7152 + img[i][j]['blue']*0.0722 )
                img[i][j]['blue'] = round(a[i][j]['red'] * 0.2126 + a[i][j]['green']*0.7152 + img[i][j]['blue']*0.0722 )
        
    if mode == 4:
        for i in range(row):
            for j in range(column):
                img[i][j]['red'] = round(a[i][j]['red'] * 0.2627 + a[i][j]['green']*0.6780 + img[i][j]['blue']*0.0593 )
                img[i][j]['green'] = round(a[i][j]['red'] * 0.2627 + a[i][j]['green']*0.6780 + img[i][j]['blue']*0.0593 )
                img[i][j]['blue'] = round(a[i][j]['red'] * 0.2627 + a[i][j]['green']*0.6780 + img[i][j]['blue']*0.0593 )
    fix(img)
    return None

def get_freq(img, channel='rgb',bin_size=16):
    row , column = get_board_size(img)
    
    binlist= []
    lvaluered= []
    lvaluegreen = []
    lvalueblue = []
    freqred = []
    freqgreen = []
    freqblue = []
    # find bin list
    i = 0
    while i < 255:
        l = [i , i + bin_size - 1]
        binlist.append(l)
        i = i + bin_size
    for i in range(row):
        for j in range(column):
            lvaluered.append(img[i][j]['red'] )
            lvaluegreen.append(img[i][j]['green'] )
            lvalueblue.append(img[i][j]['blue'] )
    lvaluered.sort()
    lvaluegreen.sort()
    lvalueblue.sort()
    #red freq 
    for k in range(bin_size):
        counter_red = 0
        for d in range(len(lvaluered)):
            if lvaluered[d] >= binlist[k][0] and lvaluered[d] <= binlist[k][1]:
                #freqred.append(1)
                counter_red += 1
        freqred.append(counter_red)
            #     continue
            # elif d ==len(lvaluered) -1 or lvaluered[d] < binlist[k][0] and lvaluered[d] > binlist[k][1]:
            #     freqred.append(0)
    #green freq
    for k in range(bin_size):
        counter_green = 0
        for d in range(len(lvaluegreen)):
            if lvaluegreen[d] >= binlist[k][0] and lvaluegreen[d] <= binlist[k][1]:
                counter_green += 1
        freqgreen.append(counter_green)
                # freqgreen.append(1)
            #     continue
            # elif d ==len(lvaluegreen) -1 or lvaluegreen[d] < binlist[k][0] and lvaluegreen[d] > binlist[k][1]:
            #     freqgreen.append(0)    
    # blue freq
    for k in range(bin_size):
        counter_blue = 0
        for d in range(len(lvalueblue) ):
            if lvalueblue[d] >= binlist[k][0] and lvalueblue[d] <= binlist[k][1]:
                counter_blue += 1
        freqblue.append(counter_blue)
            
            #     freqblue.append(1)
            #     break
            # elif d ==len(lvalueblue) -1 or lvalueblue[d] < binlist[k][0] and lvalueblue[d] > binlist[k][1]:
            #     freqblue.append(0)      
            
    #channel checker i think we dont need this 
    # red = dict(zip(['red'],[freqred]) )
    # green = dict(zip(['green'],[freqgreen]) )
    # blue = dict(zip(['blue'],[freqblue]) )
    
    lchannel = []
    for i in range(len(channel)):
        lchannel.append(channel[i])
    lchannel = set(lchannel)
    alllists = {'bin_size':bin_size , 'red': freqred, 'green': freqgreen, 'blue' : freqblue}
    if 'r'  not in lchannel:
        alllists["red"] = []
        del alllists['red']
    if 'g' not in lchannel:
        alllists["green"] = []
        del alllists['green']
    if 'b' not in lchannel:
        alllists["blue"]  = []
        del alllists['blue']
      
    return alllists
def scale_down(img, N):
    row , column = get_board_size(img)
    a = copylist(img)

    count = 0
    countc= 0
    l1 = []
    l2 = []
    sumlistred = []
    sumlistgreen = []
    sumlistblue = []
    if row % N != 0:
        maxr = row
        while maxr % N != 0:
            maxr += 1
            if maxr % N == 0:
                break
        trow = maxr - row 
        if trow > 0:
            for i in range(trow):
                a.append(a[row - 1])
                row , column = get_board_size(a)
    if column % N != 0:
        maxc = column
        while maxc % N != 0:
            maxc += 1
            if maxc % N == 0:
                break
        tcolumn = maxc - column
        if tcolumn > 0:
            for i in range(tcolumn):
                for j in range(row):
                    a[j].append(a[j][-1])
                    row , column = get_board_size(a)        
    # if row != column:
    #     maxn = max(row,column)
    #     while maxn%N != 0:
    #         maxn += 1
    #         if maxn%N == 0:
    #             break
    #     tcolumn = maxn-column
    #     trow = maxn - column
    #     if trow > 0:
    #         for i in range(trow):
    #             a.append(a[row - 1])
    #             row , column = get_board_size(img)
    #     if tcolumn > 0:
    #         for i in range(tcolumn):
    #             for j in range(row):
    #                 a[j].append(a[j][column-1])
    #                 row , column = get_board_size(img)
    while countc < row / N  :
        for i in range(countc*N,countc*N+N):
            for j in range(count*N,count*N + N):
                try:
                    sumlistred.append(a[i][j]["red"])
                except IndexError:
                    pass
        for i in range(countc*N,countc*N+N):
            for j in range(count*N,count*N + N):
                try :
                    sumlistgreen.append(a[i][j]["green"])
                except IndexError:
                    pass
        for i in range(countc*N,countc*N+N):
            for j in range(count*N,count*N + N):
                try:
                    sumlistblue.append(a[i][j]["blue"])
                except IndexError:
                    pass
                if j == count*N + N - 1 and i == countc*N+N - 1:
                    l2.append({'red':round(sum(sumlistred)/N**2) , 'green':round(sum(sumlistgreen)/N**2),'blue':round(sum(sumlistblue)/N**2)} )
                    sumlistred = []
                    sumlistgreen = []
                    sumlistblue = []
        
        count += 1
        if len(l2) == N :
            l1.append(l2)
            l2 = []
            countc += 1
            count = 0
    
    r , c = get_board_size(l1) 
    for j in range(c - (column  // N ) ):
        for i in range(r):
            l1[i].pop()
    fix(l1)
    return l1

def scale_up(img, N):
    row , column = get_board_size(img)
    a = copylist(img)
    rowscale=[]
    
    count = 0
    for i in range(row):
        for j in range(N):
            rowscale.append(a[i])
    row , column = get_board_size(rowscale)
    b =copylist(rowscale)
    for i in range(row):
        
        for j in range(column):
            for x in range(N-1):
                b[i].insert(count,rowscale[i][j])
            count +=N
        count = 0        
    fix(b)
    return b 
def expand(img):
    a = copylist(img)
    rowexpand=[]
    row , column = get_board_size(img)
    for i in range(row):
        if i == 0 or i == row  -1:
            for x in range(2):
                rowexpand.append(a[i])
        else:
            rowexpand.append(a[i])
    columnexpand =[]
    row , column = get_board_size(rowexpand)
    for i in range(row):
        columnexpand[i].insert(0,)
    return rowexpand
def apply_window(img, window):
    pass
