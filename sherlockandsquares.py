# int a: the lower range boundary
# int b: the upper range boundary

import math


def squares(a, b):
    count = 0
    for i in range(a, b+1):
        a = math.sqrt(i)
        b = int(a)
        if abs(len(str(b)) - len(str(a))) == 2:
            count += 1

    return count
print(squares(24,49))