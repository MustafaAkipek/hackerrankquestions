# int x: Cat A's position
# int y: Cat B's position
# int z: Mouse C's position

def catAndMosue(x,y,z):
    if abs(x-z) < abs(y-z):
        return ("Cat A")
        
    elif abs(y-z) < abs(x-z):
        return ("Cat B")
        
    else:
        return ("Mouse C")
        
print(catAndMosue(1,3,2))