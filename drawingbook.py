# int n: the number of pages in the book
# int p: the page number to turn to 

def pageCount(n ,p):
    dif = n-p
    res = dif/2
    if dif < 2:
        if p % 2 == 1:
            if n > p:
               return  1
            else:
                return 0
        if p % 2 == 0:
            if n > p:
                return 0
            else:
                return 1
    
    return res
                 

print(pageCount(5, 4))