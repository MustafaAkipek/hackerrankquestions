# int arr[n]: an array of integers

def plusMinus(arr):
    presult = 0
    nresult = 0
    zeron = 0
    
    for i in range(0,5):
        if arr[i] > 0:
            presult += 1
        if arr[i] == 0:
            zeron += 1
        if arr[i] < 0:
            nresult += 1
            
    positiveration = presult/len(arr)
    negativeration = nresult/len(arr)
    zeroration = zeron/len(arr) 
       
    return f"{positiveration:.6f}\n{negativeration:.6f}\n{zeroration:.6f}"
    
print(plusMinus([1, 1, 0, -1, -1]))