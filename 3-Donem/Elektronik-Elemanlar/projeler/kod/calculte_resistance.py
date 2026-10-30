import numpy as np
list_of_resistances =np.zeros((600,600))

def nearest_number(arr, target):
    # Find the distance between the target and each element in the array
    distances = np.abs(arr - target)
    
    # Find the index of the element with the minimum distance
    min_index = np.argmin(distances)
    
    # Get the element at the minimum index
    nearest_number = arr.flat[min_index]
    
    return nearest_number

for i in range(1,600):
    for j in range(1,600):
        R1 = i*1000
        R2 = j*1000
        value = (R1*(R2**2)) / ((R1+R2)**2)
        #print(value)
        list_of_resistances[i][j] = value
#print(list_of_resistances)
print(nearest_number(list_of_resistances, 0.9))
