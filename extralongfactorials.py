# n: an integer

def extraLongFactorials(n):
    # Write your code here
    a = 1
    for i in range(1, n+1):
        a *= i
        
    print(a)
    
extraLongFactorials(25)