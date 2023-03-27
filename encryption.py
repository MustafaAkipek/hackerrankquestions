# string s: a string to encrypt

import math

def encryption(s):
    text = []
    for i in range(len(s)):
        if s[i] != " ":
            text.append(s[i])
            
    row = math.floor(math.sqrt(len(text)))
    column = math.ceil(math.sqrt(len(text)))
    return None

print(encryption("haveaniceday"))