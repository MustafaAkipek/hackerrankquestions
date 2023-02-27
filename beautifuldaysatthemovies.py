# int i: the starting day number
# int j: the ending day number
# int k: the divisor

def beautifulDays(i, j, k):
    niceday = 0
    
    for d in range(i, j+1):
        stringd = str(d)[::-1]
        day = abs(int(stringd) - d)
        if day % k == 0:
            niceday += 1
            
    return niceday

print(beautifulDays(20, 23 , 6))