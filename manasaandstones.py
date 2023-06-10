# int n: the number of non-zero stones
# int a: one possible integer difference
# int b: another possible integer difference

def stones(n, a, b):
    result = set()

    for i in range(n):
        result.add(i*a + (n-1-i)*b)

    return sorted(list(result))

print(stones(3, 1, 2))

# my solution but dont support 4 case(because of the repetitive elements)
"""
res = []
    for k in range(n):
        for m in range(n-k):
            if k + m == n-1:
                l = a * k + m * b
                res.append(l)

    res.sort()

    return res
"""