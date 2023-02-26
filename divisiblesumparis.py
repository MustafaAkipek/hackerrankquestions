# int n: the length of array ar
# int ar[n]: an array of integers
# int k: the integer divisor

def divisibleSumPairs(n, k, ar):
    pair = 0
    
    for i in range(n):
        for j in range(i+1, n):
            if (ar[i] + ar[j]) % k == 0:
                pair += 1
                
    return pair

print(divisibleSumPairs(6, 5, [1,2,3,4,5,6]))