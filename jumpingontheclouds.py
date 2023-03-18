# int c[n]: an array of binary integers

def jumpingOnClouds(c):
    jump = 0
    i = 0
    over = True
    
    while(over):
        if len(c) == 2:
            i += 1
            jump += 1
            break
            
        if c[i+1] == 1:
            i += 2
            jump += 1
            
        elif c[i+2] == 1:
            i += 1
            jump += 1
            
        else:
            i += 2
            jump += 1
            
        if len(c) - i == 2:
            i += 1
            jump += 1
            over = False
            
        if i == len(c) -1:
            over = False

    return jump
            
print(jumpingOnClouds([0,0,1,0,0,1,0]))