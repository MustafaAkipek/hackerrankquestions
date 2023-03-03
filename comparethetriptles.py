# int a[3]: Alice's challenge rating
# int b[3]: Bob's challenge rating

def compareTriplets(a, b):
    timer_a = 0
    timer_b = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            timer_a += 1
        elif b[i] > a[i]:
            timer_b += 1
            
    return timer_a, timer_b

print(compareTriplets([1,2,3],[3,2,1]))