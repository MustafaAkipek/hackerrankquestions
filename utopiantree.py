# int n: the number of growth cycles to simulate

def utopianTree(n):
    stage = 0
    height = 1
    while (stage < n):
        stage += 1
        if stage % 2 == 0:
            height += 1
        else:
            height *= 2
    
    return height

print(utopianTree(4))