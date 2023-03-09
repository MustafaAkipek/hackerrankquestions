# int n: the number of pages in the book
# int p: the page number to turn to

def pageCount(n, p):
    total = n / 2
    total = int(total)
    
    left = p / 2
    left = int(left)
    
    right = total - left
    right = int(right)
    
    return min(left, right)
    
print(pageCount(6, 2))