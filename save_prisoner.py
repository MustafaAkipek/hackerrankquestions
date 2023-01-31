def saveTheProisoner(n, m, s):
    liste = [i for i in range(1,n+1)]  
    m = m % n  
    while m != 0: 
        s += 1  
        m -= 1  
    return (liste[s-2])   
    
print(saveTheProisoner(3, 7, 3))