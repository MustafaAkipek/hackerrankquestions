from collections import Counter

def migratoryBirds(arr):
    nlist = [0] * len(arr)
   
    for i in range(len(arr)):
        nlist[arr[i]] += 1
    
    return nlist.index(max(nlist))
    
   
print(migratoryBirds(arr=[1, 1, 2, 2, 3]))

