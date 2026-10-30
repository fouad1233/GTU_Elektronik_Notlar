def systemverilog_thruth_table_generator(variables,time):
    matrix = []
    for i in range(2**len(variables)//2):
        matrix[0].append([0])
    for i in range(2**len(variables))//2:
        matrix[0].append([1])
        
    for i in range(2**len(variables)//2):
        matrix[0].append([0])
    for i in range(2**len(variables))//2:
        matrix[0].append([1])
def remaker(message):
    for i in message :
        if i == '+':
            message = message.replace(i,'or ')
        elif i == '&':
            message = message.replace(i,'and ')
    #for i in range(len(message) - 1):
    #    if message[i] == "'":
    #        #delete the character
    #        message = message.replace(message[i-1],message[i-1]+'~')
    #        message = message.replace(message[i],'')
    #        
    #        print(message)
    return message
print(remaker("Y(PoS) = (G'+T+U'+E) & (G'+T+U'+E') & (G'+T'+U'+E) & (G'+T'+U'+E')"))