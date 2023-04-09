# int p: the lower limit 
# int q: the upper limit

import math

def kaprekarNumbers(p, q):
    kaprekarn = []

    for i in range(p, q):
        li = len(str(i))
        i = i ** 2

        
        if len(str(i)) == 1:
            if i ** 2 == i:
                print(i, end=" ")

        elif len(str(math.sqrt(i))) % 2 != 1:
            stri = str(i)
            first = stri[:li]
            second = stri[li:]

            fn = int(first)
            sn = int(second)

            si = math.sqrt(i)
            if fn + sn == int(si):
                print(int(si), end= " ")

kaprekarNumbers(1, 100)