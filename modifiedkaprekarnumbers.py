# int p: the lower limit 
# int q: the upper limit

import math

def kaprekarNumbers(p, q):
    res = []

    for i in range(p, q+1):
        sqr = str(i ** 2)
        n = len(sqr)

        if i == 1:
            res.append(i)
        elif n > 1 and i == int(sqr[:n//2]) + int(sqr[n//2:]):
            res.append(i)

    if len(res) == 0:
        print("INVALID RANGE")
    else:
        print(*res)

kaprekarNumbers(1, 100)