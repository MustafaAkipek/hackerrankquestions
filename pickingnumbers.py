from collections import Counter

def pickingNumbers(a):
    newarr = Counter(a) #{1: 2, 2: 2, 3: 1}
    maxnumber = 0
    
    for i in range(100):
        maxnumber = max(maxnumber, newarr[i] + newarr[i+1]) 
        
    return maxnumber

# Beta sürümü
"""
def pickingNumbers(a):
    newlist = list(set(a)) # newlist = (1,2,4,5)
    count = 0
    for i in range(len(newlist) - 1):
        if abs(newlist[i] - newlist[i+1]) <= 1:
            current = a.count(newlist[i]) + a.count(newlist[i+1])
            if current > count:
                count = current
    return count
"""
print(pickingNumbers([1, 2, 2, 3, 1]))    