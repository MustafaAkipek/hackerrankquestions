# bill: an array of integers representing the cost of each item ordered
# k: an integer representing the zero-based index of the item Anna doesn't eat
# b: the amount of money that Anna contribured to the bill

def bonAppetit(bill, k, b):
    nbill = sum(bill) - bill[k] 
    dbill = nbill / 2
    if dbill == b:
        print("Bon Appetit")
    else:
        abill = sum(bill)
        obill = abill / 2
        print(int(obill - dbill))
        
bonAppetit([2,4,6],2,6)