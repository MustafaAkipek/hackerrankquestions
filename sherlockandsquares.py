# int a: the lower range boundary
# int b: the upper range boundary

def squares(a, b):
    pass

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