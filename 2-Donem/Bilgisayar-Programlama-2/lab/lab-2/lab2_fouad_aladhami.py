my_name = "Fouad Aladhami"
my_id = "210102002808"
my_email = "f.aladhami2021@gtu.edu.tr"
import random,string,time,heapq
import matplotlib.pyplot as plt
def problem1(n, wmin= 1, wmax=10,tflag = 0,):
    string_letters =  string.digits + string.ascii_letters 
    rl = []
    if tflag ==0:#string
        for i in range(n):
            element = ''.join(random.choice(string_letters) for i in range(random.randint(wmin,wmax) ))
            rl.append(element)
    elif tflag == 1:#integer
        for i in range(n):
            rl.append(random.randint(wmin,wmax))
    elif tflag == 2 :#float
        for i in range(n):
            rl.append(random.uniform(wmin,wmax))
    return rl
def problem2(rl):
    t1 = time.perf_counter_ns()
    
    for i in range(1,len(rl)):
        a = rl[i]
        j = i - 1
        while j >=0 and a < rl[j]:
            rl[j + 1] = rl[j]
            j -= 1
        rl[j+ 1] = a
            
    t2 = time.perf_counter_ns()
    t = t2 - t1
    return t
def problem3(rl):
    t1 = time.perf_counter_ns()
    for i in range(len(rl)):
        cur = rl.pop(i)
        j = i-1
        while j >=0 and rl[j] > cur:
            j -= 1
        rl.insert(j+1, cur)
    t2 = time.perf_counter_ns()
    t = t2 - t1
    return t
def problem4(rl):
    t1 = time.perf_counter_ns()
    for i in range (len(rl)):
        j = i - 1
        selected = rl[i]
        insert_loc = binarySearch(rl, selected, 0, j)
        while (j >= insert_loc):
            rl[j + 1] = rl[j]
            j-=1
        rl[j + 1] = selected
    t2 = time.perf_counter_ns()
    t = t2-t1
    return t
def binarySearch(a, item, low, high):
    while (low <= high):
        mid = low + (high - low) // 2
        if (item == a[mid]):
            return mid + 1
        elif (item > a[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return low
def problem5(rl):
    t1 = time.perf_counter_ns()
    rl.sort()
    t2 = time.perf_counter_ns()
    t = t2-t1
    return t
def problem6(rl):
    a = rl.copy()
    heapq.heapify(a)
    b = []
    t1 = time.perf_counter_ns()
    for value in a:
        heapq.heappush(b, value)
    b = [heapq.heappop(b) for i in range(len(b))]
    t2 = time.perf_counter_ns()
    t = t2 - t1
    return b ,t 
def problem6_e(rl):
    
    b = []
    t1 = time.perf_counter_ns()
    for value in rl:
        heapq.heappush(b, value)
    b = [heapq.heappop(b) for i in range(len(b))]
    t2 = time.perf_counter_ns()
    t = t2 - t1
    return b ,t 
# #plot graphs
# t1 = time.perf_counter()
# y = []
# x2 = []
# x3 = []
# x4 = []
# x5 = []
# x6 = []
# for i in range(0,10**5,10000):
#     y.append(i)
#     rl = problem1(i)
#     a = rl.copy()
#     x2.append(problem2(a)/10**9)
#     a = rl.copy()
#     x3.append(problem3(a)/10**9)
#     a = rl.copy()
#     x4.append(problem4(a)/10**9)
#     a = rl.copy()
#     x5.append(problem5(a)/10**9)
#     a = rl.copy()
#     x6.append(problem6(a)[1]/10**9)
# plt.plot( y,x2, label = "Insertion Sort by pair wise swaps")
# plt.plot( y,x3, label = "Insertion Sort by pair wise comp. & pop/insert")
# plt.plot( y,x4, label = "Insertion Sort by binary search")
# plt.plot( y,x5, label = "Merge Sort")
# plt.plot( y,x6, label = "Heap Sort")
# plt.ylabel('time')
# # naming the y axis
# plt.xlabel('lengh of list')
# #title
# plt.title('graph of sort algorithms efficiency')
# # show a legend on the plot
# plt.legend()

# # function to show the plot
# plt.show()
# t2 = time.perf_counter()
# t = t2 - t1
# print("You plot the graph in ",t, "seconds")

# if __name__ == "__main__":
#     print(f"My name is {my_name}.")
#     print(f"My number is {my_id}.")
#     print(f"My email is {my_email}.")
    







