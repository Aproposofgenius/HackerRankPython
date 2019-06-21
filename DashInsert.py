def DashInsert(str): 
    final=str[0]
    odd ='13579'
    counter = 1
    # code goes here 
    for i in range(1, len(str)):
        if final[counter-1] in odd and str[i] in odd:
            final+='-'
            final+=str[i]
            counter+=2
            
        else:
            final+=str[i]
            counter+=1
        
    
    return final
    
# keep this function call here  
print DashInsert(raw_input())
