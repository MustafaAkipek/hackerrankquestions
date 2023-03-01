# int a[n]: the array to rotate
# int k: the rotation count
# int queries[q]: the indices to report

def circularArrayRotation(a, k, queries):
    nlist = []
    for i in range(k):
        n = a[len(a)-1]
        a.insert(0, n)
        a.pop()
        
    for i in range(len(queries)):
        m = queries[i]
        nlist.append(a[m])
    
    return nlist
        
print(circularArrayRotation([3,4,5],2,[1,2]))