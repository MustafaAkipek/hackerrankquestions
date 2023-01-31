arr = [1,2,3,4,5]

def miniMaxSum(arr):
    sum = 0
    result = []
    for i in range(len(arr)):
        sum += arr[i]
    
    for i in range(len(arr)):
        result.append(sum - arr[i])
        
    print(min(result), max(result))
    
miniMaxSum(arr)
        
        