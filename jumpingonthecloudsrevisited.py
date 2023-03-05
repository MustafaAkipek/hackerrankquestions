# int c[n]: the cloud types along the path
# int k: the length of one jump

def jumpingOnClouds(c, k):
    energy = 100
    i = 0
    over = True
    
    while(over):
        i += k
        
        if(i<len(c)):
            if(c[i] == 0):
                energy -= 1
            else:
                energy -= 3
                
        else:
            i = i % len(c)
            if(c[i] == 0):
                energy -= 1
            else:
                energy -= 3
                
        if(i == 0):
            over = False
        
    return energy

print(jumpingOnClouds([1, 1, 1, 0, 1, 1, 0, 0, 0, 0],3))