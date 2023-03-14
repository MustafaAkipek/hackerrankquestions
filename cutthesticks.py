# int arr[n]: the lengths of each stick
from collections import Counter

def cutTheSticks(arr):
    result = []
    n = len(arr)
    s = Counter(arr)
    
    for i in sorted(s.keys()):
        result.append(n)
        n -= s[i]
        
    return result
        
print(cutTheSticks([5, 4, 4, 2, 2, 8]))