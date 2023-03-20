# s: a string to repeat
# n: the number of characters to consider

def repeatedString(s, n):
    length = len(s)
    repeat = int(n / length)
    count = 0
    remain = 0
    
    for i in range(len(s)):
        if s[i] == "a":
            count += 1
        
    alla = count * repeat

    if n % length != 0:
        remain = n % length
        
    for i in range(remain):
        if s[i] == "a":
            alla += 1
    
    return alla    
        
print(repeatedString("aba", 10))