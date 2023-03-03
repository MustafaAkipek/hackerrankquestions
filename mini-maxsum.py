# arr: an array of 5 integers

def miniMaxSum(arr):
    sum = 0
    result = []
    for i in range(len(arr)):
        sum += arr[i]
    
    for i in range(len(arr)):
        result.append(sum - arr[i])
        
    print(min(result), max(result))
    
miniMaxSum([1,3,5,7,9])  