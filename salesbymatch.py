# int n: the number of the socks in the pile
# int ar[n]: the colors of each sock

from collections import Counter

def sockMerchant(n, ar):
    narr = Counter(ar) # ({10: 4, 20: 3, 30: 1, 50: 1})
    pair = 0
    
    for i in range(101):
        while(narr[i] >= 2):
            pair += 1
            narr[i] -= 2
            
    return pair

print(sockMerchant(9, [10,20,20,10,10,30,50,10,20])) 