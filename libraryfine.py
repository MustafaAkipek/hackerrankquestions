# d1,m1,y1: returned date day, month and year, each an integer
# d2,m2,y2: due date day, month and year, each an integer

def libraryFine(d1, m1, y1, d2, m2, y2):
    if m1 == m2 and y1 == y2:
        if d1-d2 <= 0:
            return 0
        else:
            return (d1-d2) * 15

    if m1 != m2 and y1 == y2:
        if m1-m2 <= 0:
            return 0
        else:
            return (m1-m2) * 500
        
    if y1 != y2:
        if y1-y2 <= 0:
            return 0
        else:
            return (y1-y2) * 10000
            
print(libraryFine(14,7,2018,5,7,2018))