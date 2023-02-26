# int n: an integer

def staircase(n):
    i = 1 
    j = n-1 
    while(i <= n):
        print(" "*(j)+i*"#")
        i += 1
        j -= 1

staircase(4)