# int s[n] = the numbers on each of the squares of chocolate
# int d: Ron's birth day
# int m: Ron2s birth month

def subarray_division(s, d, m):
    i = 0
    dw = 0
    
    while m <= len(s):
        if sum(s[i:m]) == d:
            dw += 1
        i += 1
        m += 1
    
    return dw
 
print(subarray_division([1, 2, 1, 3, 2], 3, 2))