# int x1, int v1: starting position and jump distance for kangaroo 2
# int x2, int v2: starting position and jump distace for kangaroo 2

def numberlinejumps(x1, v1, x2, v2):
    for i in range(10000):
        x1 += v1
        x2 += v2
        if x1 == x2:
            return "YES"
    else:
        return "NO"

print(numberlinejumps(0, 3, 4, 2))