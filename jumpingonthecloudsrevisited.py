# int c[n]: the cloud types along the path
# int k: the length of one jump

def jumpingOnClouds(c, k):
    path = 0
    for i in range(0, len(c), k):
        if i < len(c):
            path += 1
            if c[i] == 1:
                path += 2
                
    return 100-path

print(jumpingOnClouds([1 ,1 ,1 ,0 ,1 ,1 ,0 ,0 ,0 ,0],3))