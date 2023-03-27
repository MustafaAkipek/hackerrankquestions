# string s: a string to encrypt
"""
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
"""

"""
# Create an empty 2D list with 3 rows and 2 columns 
empty_2d_list = [[] for _ in range(3)] 
 
# Add elements to the list 
empty_2d_list[0].append(1) 
empty_2d_list[0].append(2) 
empty_2d_list[0].append(10) 
empty_2d_list[1].append(3) 
empty_2d_list[1].append(4) 
empty_2d_list[2].append(5) 
empty_2d_list[2].append(6) 

print(empty_2d_list)
"""

s = [[2][3]] 
print(s)