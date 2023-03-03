# int p[n]: an array of integers

def permutationEquaiton(p):
    b = []
    for x in range(1, len(p)+1):
        a = p.index(x) + 1
        b.append(p.index(a) + 1)
            
    return b

print(permutationEquaiton([5,2,1,3,4])) 