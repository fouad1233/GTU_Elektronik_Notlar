f = open("values.txt")
def calculte_error(true_v,measured ):
    return round(( ( (true_v - measured)/true_v )* 100) , 3 )

for line in f:
    li_of_values = line.replace("V" , '').replace("mW" , '').replace("mA" , '').split()
    #print(li_of_values)
    error_p = calculte_error(float(li_of_values[0]),float(li_of_values[1]) )
    print("% "+str(error_p))
    

f.close()

