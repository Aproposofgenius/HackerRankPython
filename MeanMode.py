import numpy as np 
from collections import Counter 

def MeanMode(arr): 
    arr = np.array(arr)
    data = Counter(arr) 
    get_mode = dict(data)
    mode = [k for k, v in get_mode.items() if v == max(list(data.values()))] 
    if np.mean(arr) == mode[0]:
        return 1
        
    else:    # code goes here 
        return 0
# keep this function call here  
print MeanMode(raw_input())
