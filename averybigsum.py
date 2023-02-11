# int ar[n]: an array of integers

def aVeryBigSum(ar):
    result = 0
    for i in range(len(ar)):
        result += ar[i]
    return result

print(aVeryBigSum([1000000001, 1000000002, 1000000003, 1000000004, 1000000005]))