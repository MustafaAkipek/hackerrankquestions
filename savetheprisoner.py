# int n = number of prisoners
# int m = the number of sweets
# int s = the chair number to begin passing out sweets from

def saveTheProisoner(n, m, s):
    c = m % n
    if((c + s - 1) % n == 0): # because prisoners not have 0 number. so 0 is meaning last prisoner
        return n
    else:
        return (c + s - 1) % n
        
print(saveTheProisoner(3, 7, 3))


# My solution but not support time limit
"""
candy = m % n
    candy -= 1
    while(candy != 0):
        s += 1
        candy -= 1
    else:
        return s
"""
