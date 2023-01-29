def catAndMosue(x,y,z):
    if abs(x-z) < abs(y-z):
        print("Cat A")
        
    elif abs(y-z) < abs(x-z):
        print("Cat B")
        
    else:
        print("Mouse C")
        
catAndMosue(1,3,2)