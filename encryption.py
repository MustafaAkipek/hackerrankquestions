# string s: a string to encrypt

import math

def encryption(s):
    l = len(s)
    f = math.floor(math.sqrt(l))
    c = math.ceil(math.sqrt(l))
    result = []

    for i in range(c):
        text = []
        j = 0
        while (i+j) < l:
            if s[i+j] != " ":
                text.append(s[i+j])
            j += c
        result.append("".join(text))

    return " ".join(result)

print(encryption("feedthedog  "))