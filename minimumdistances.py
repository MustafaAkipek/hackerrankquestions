# int a[n]: an array of integers

def minimumDistances(a):
    dis = []
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
                dis.append(abs(i-j))

    if len(dis) != 0:
        return min(dis)
    else:
        return -1

print(minimumDistances([3,2,1,2,3]))