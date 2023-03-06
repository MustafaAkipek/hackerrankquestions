# int n: the value of to analyze

def findDigits(n):
    timer = 0
    l = len(str(n))
    
    for i in range(l):
        n = str(n)
        if int(n[i]) != 0:
            if int(n) % int(n[i]) == 0:
                timer += 1
        
    return timer
    
print(findDigits(124))