def migratoryBirds(arr):
    nlist = [0] * len(arr)
    
    for i in range(len(arr)):
        nlist[arr[i]] += 1
        
    return nlist.index(max(nlist))
    
print(migratoryBirds([1, 4, 4, 4, 5, 3]))