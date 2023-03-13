# int a: the lower range boundary
# int b: the upper range boundary

import math

def squares(a, b):
    return math.floor(math.sqrt(b)) - math.ceil(math.sqrt(a)) + 1

print(squares(24,49))

# my solution but not support time limit exceeded
"""
    i = 0
    count = 0
    
    while(i < b):
        i += 1
        if i*i >= a and i*i <= b:
            count += 1
            
    return count
"""