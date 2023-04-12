# int d: the value to match
# int arr[n]: the sequence, sorted ascending

def beautifulTriplets(d, arr):
    count = 0
    for i, val1 in enumerate(arr[:-2]):
        for j, val2 in enumerate(arr[i+1:-1], start=i+1):
            if val2 - val1 != d:
                continue
            for val3 in arr[j+1:]:
                if val3 - val2 == d:
                    count += 1
    return count

print(beautifulTriplets(1, [2,2,3,4,5]))