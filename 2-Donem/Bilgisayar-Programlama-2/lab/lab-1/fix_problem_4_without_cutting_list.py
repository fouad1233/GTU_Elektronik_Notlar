import random 
def problem1(x):
    """
    Write a function that takes an integer nas an input
    and returns a one dimensional list with random integer entriesin [0:1000].
    You can use randomlibrary.
    ●Function parameter names do not matter,
    but the function should expect 1 parameter.
    ●Function won’t be tested for exceptional cases.
    ●input  :○n ∈ℤand n∈[1:104]
    ●output : x = { x : x is a list and x[i] ∈[0:1000]}
    >>> rl = problem1(3)
    """
    number_list = []
    for i in range(x):
        number_list.append(random.randint(0, 1000))
    return number_list


def problem4(rl, n = None):
    """
    >>> rl= [293, 170, 207, 323, 963, 445, 351, 921, 165, 759]
    >>> valloc,loclist=problem4(rl)
    >>> print(valloc)
    (963, 4)
    >>> print(loclist)
    [5, 2, 4]
    >>> rl=[0,1,2,3,4,5,6,7,8,9]
    >>> valloc,loclist=problem4(rl)
    >>> print(valloc)
    (9, 9)
    >>> print(loclist)
    [5, 8, 9]
    
    >>> rl=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    >>> valloc,loclist=problem4(rl)
    >>> print(valloc)
    (16, 16)
    >>> print(loclist)
    [8, 12, 14, 16]
    
    Parameters
    ----------
    rl : list
    n : integer 'the starting index'
    

    Returns
    -------
    None.

    """
    if n == None:
        n = round(len(rl)/2)
    if n >= len(rl):
        return IndexError
    
    peak = 0
    peak_index = ()
    tested_indices = []
    distance_list = []
    direction_list = []
    while True:
        tested_indices.append(n)
        if len(tested_indices) >= 2:
            distance_list = []
            for i in range(len(tested_indices) ):
                distance_list.append(tested_indices[-1] -tested_indices[i] )
                
        if n < len(rl) -1 and n > 0 :
            if rl[n] >= rl[n+1] and rl[n] >= rl[n-1]:
                peak_index = n 
                peak = rl[n]
                return ( (peak, peak_index) , tested_indices )
                
            elif rl[n]<rl[n-1] and n != 0:
                direction_list.append('left')
                
                if len(direction_list) >= 2:
                    left_near = []
                    for i in range(len(distance_list)):
                        if distance_list[i] > 0 :
                            left_near.append(distance_list[i])
                    if len(left_near) >= 1:
                        n2 = min(left_near)
                    if direction_list[-1] != direction_list[-2]:
                        if len(left_near) >= 1:
                            n = round( (tested_indices[-1] + n2 + tested_indices[-1]) / 2)
                        else:
                            n = round( (tested_indices[-1] + tested_indices[-2]) / 2)
                    else : 
                        
                        n=round((n-1)/2)
                else :
                    n=round((n-1)/2)
            elif  rl[n]<rl[n+1] and n !=len(rl)-1:
                direction_list.append('right')
                
                if len(direction_list) >= 2:
                    right_near = []
                    for i in range(len(distance_list)):
                        if distance_list[i] < 0 :
                            right_near.append(distance_list[i])
                    if len(right_near) >= 1:
                        n2 = max(right_near)
                        
                    if direction_list[-1] != direction_list[-2]:
                        if len(right_near) >= 1:
                            n = round( (tested_indices[-1] - n2 +tested_indices[-1]) / 2)
                        else : 
                            n=round( (n + len(rl) ) / 2)
                    else : 
                        
                        n=round( (n + len(rl) ) / 2)
                else :
                    n=round( (n + len(rl) ) / 2)
                    
            else:
                return 'Peak not founded'
            
              
        elif n == len(rl) - 1 and  rl[n] >= rl[n-1]:
             peak_index = n 
             peak = rl[n]
             return ( (peak, peak_index) , tested_indices )
        elif n == len(rl) - 1  and rl[n] < rl[n -1 ]:
            direction_list.append('left')
            
            if len(direction_list) >= 2:
                left_near = []
                for i in range(len(distance_list)):
                    if distance_list[i] > 0 :
                        left_near.append(distance_list[i])
                if len(left_near) >= 1:
                    n2 = min(left_near)
                if direction_list[-1] != direction_list[-2]:
                    if len(left_near) >= 1:
                        n = round( (tested_indices[-1] + n2 + tested_indices[-1]) / 2)
                    else:
                        n = round( (tested_indices[-1] + tested_indices[-2]) / 2)
                else : 
                    
                    n=round((n-1)/2)
            else :
                n=round((n-1)/2)
        elif n == 0 and  rl[n] < rl[n+1]:
             direction_list.append('right')
             
             if len(direction_list) >= 2:
                 right_near = []
                 for i in range(len(distance_list)):
                     if distance_list[i] < 0 :
                         right_near.append(distance_list[i])
                 if len(right_near) >= 1:
                     n2 = max(right_near)
                     
                 if direction_list[-1] != direction_list[-2]:
                     if len(right_near) >= 1:
                         n = round( (tested_indices[-1] - n2 +tested_indices[-1]) / 2)
                     else : 
                         n=round( (n + len(rl) ) / 2)
                 else : 
                     
                     n=round( (n + len(rl) ) / 2)
             else :
                 n=round( (n + len(rl) ) / 2)
        elif n== 0 and rl[n]>=rl[n+1]:
             peak_index = n 
             peak = rl[n]
             return ( (peak, peak_index) , tested_indices )
        elif len(rl) ==  1 :
            peak_index = n 
            peak = rl[n]
            return ( (peak, peak_index) , tested_indices )
        else:
             return 'Peak not founded'
print(problem4([377, 903, 69, 367, 520, 641, 309, 653, 986, 499, 339, 678, 138, 124, 293, 98, 681, 778, 341, 617, 225, 114, 6, 468, 782, 666, 377, 564, 588, 824, 127, 636, 945, 549, 434, 73, 522, 200, 228, 449, 340, 568, 454, 908, 47, 587, 571, 537, 425, 719, 258, 763, 519, 402, 366, 904, 192, 294, 480, 956, 893, 494, 417, 945, 308, 951, 958, 938, 498, 799, 454, 80, 771, 393, 788, 453, 33, 292, 774, 272, 381, 211, 352, 998, 428, 254, 180, 642, 254, 993, 297, 68, 139, 195, 394, 524, 815, 316, 928, 305, 768, 972, 288, 238, 898, 552, 812, 263, 176, 19, 226, 940, 477, 974, 174, 580, 497, 93, 865, 678, 234, 487, 698, 579, 994, 737, 60, 84, 500, 707, 640, 204, 318, 561, 905, 165, 730, 205, 667, 674, 452, 620, 835, 600, 447, 925, 648, 64, 492, 499, 119, 713, 854, 634, 419, 91, 198, 594, 380, 147, 909, 34, 513, 912, 220, 382, 765, 589, 462, 447, 916, 489, 33, 983, 305, 338, 891, 665, 101, 398, 751, 140, 572, 898, 766, 879, 111, 835, 793, 75, 266, 430, 39, 246, 906, 103, 698, 593, 787, 823, 392, 864, 659, 941, 873, 537, 44, 746, 696, 898, 692, 958, 979, 985, 737, 169, 768, 176, 302, 948, 429, 628, 953, 253, 211, 919, 611, 314, 266, 986, 738, 359, 505, 86, 194, 989, 334, 313, 767, 223, 933, 785, 721, 214, 96, 622, 631, 13, 167, 143, 771, 857, 128, 420, 186, 380, 28, 106, 683, 202, 465, 172, 175, 875, 798, 856, 639, 437, 99, 95, 748, 346, 965, 248, 605, 594, 281, 675, 461, 401, 248, 392, 552, 502, 665, 556, 702, 491, 326, 435, 508, 990, 871, 865, 144, 936, 473, 138, 119, 154, 399, 317, 243, 650, 822, 913, 718, 195, 153, 836, 615, 727, 192, 422, 78, 35, 794, 475, 603, 211, 599, 342, 870, 21, 654, 746, 818, 395, 682, 148, 357, 206, 646, 383, 517, 898, 338, 828, 599, 547, 926, 537]))
if __name__ == "__main__":
    for i in range(5,1000):
        rl = problem1(i)
        print(rl)
        print(problem4(rl, i -2 ))

    # We run the print on the function since we will be returning the value
    # and print() function will print whatever is passed within its parentheses.
    import doctest
    doctest.testmod()
    