# string s: a string to encrypt

import math

def encryption(s):
    text = []
    for i in range(len(s)):
        if s[i] != " ":
            text.append(s[i])
            
    row = math.floor(math.sqrt(len(text)))
    column = math.ceil(math.sqrt(len(text)))
    
    matris= empty_2d_list = [[] for _ in range(row)]
    
    m = 0
    
    while():
        matris[m].append(text[i])
        if m
    print(matris) 
    
    
print(encryption("haveaniceday"))