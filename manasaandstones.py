# int n: the number of non-zero stones
# int a: one possible integer difference
# int b: another possible integer difference

def stones(n, a, b):
    res = []
    for k in range(n):
        for m in range(n-k):
            if k + m == n-1:
                l = a * k + m * b
                res.append(l)

    res.sort()

    return res

print(stones(3, 1, 2))