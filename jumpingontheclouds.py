# int c[n]: an array of binary integers

def jumpingOnClouds(c):
    jump = 0
    i = 0
    
    while(len(c) - i > 2):
        if c[i+1] == 1:
            i += 2
            jump += 1
            
        elif c[i+2] == 1:
            i += 1
            jump += 1
            
        else:
            i += 2
            jump += 1
            
    if i == len(c) - 1:
        return jump
    else:
        jump += 1
        return jump
            
print(jumpingOnClouds([0,0,1,0,0,1,0]))