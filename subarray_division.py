def subarray_division(s, d, m):
    i = 0
    j = m
    count = 0
    
    while j <= len(s):
        if sum(s[i:j]) == d:
            count += 1
        i += 1
        j += 1
    
    return count

print(subarray_division([1, 2, 1, 3, 2], 3, 2))
