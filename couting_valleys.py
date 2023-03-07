# int steps: the number of steps on the hike
# string path: a string describing the path

def countingValleys(steps, path):
    level = 0  
    valleys = 0  
    
    for step in path:
        if step == 'U':
            level+=1
            if level == 0:
                valleys+=1
                
        else:
            level-=1
    
    return (valleys)

print(countingValleys(8, "UDDDUDUU"))