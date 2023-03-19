# int arr[n]: an array of integers

from collections import Counter

def equalizeArray(arr):
    narr = Counter(arr)
    mrn = max(narr.values())
    
    return len(arr) - mrn
            
print(equalizeArray([1,2,2,3]))