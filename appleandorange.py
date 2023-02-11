# s: integer, starting point of Sam's house location
# t: integer, ending location of Sams's house location
# a: integer, location of the Apple tree
# b: integer, location of the Orange tree
# apples: integer array, distances at which each apple falls from the tree
# oranges: integer array, distances at which each oragne falls from the tree

def countApplesAndOranges(s, t, a, b, apples, oranges):
    fallapples = 0
    falloranges = 0
    for i in range(len(apples)):
        if a+apples[i] >=s and a+apples[i] <= t:
            fallapples += 1
        else:
            pass
        
    for i in range(len(oranges)):
        if b+oranges[i] >= s and b+oranges[i] <= t:
            falloranges += 1
        else:
            pass
        
    print(fallapples)
    print(falloranges)
        
             
countApplesAndOranges(7, 10, 4, 12, [2, 3, -4], [3, -2, -4])