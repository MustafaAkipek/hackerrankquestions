# int n: the size of the width array
# int cases[t][2]: each element containes the starting and ending incides for a segment to consider, inclusive

def serviceLane(n, cases):
    res = []
    for i in range(len(cases)):
        s = cases[i][0]
        e = cases[i][1]
        widthes = []
        for i in range(s, e+1):
            widthes.append(n[i]) # note: width is not embedded, so I wrote n, but on hackerrank you write width 
        res.append(min(widthes))

    return res
        
print(serviceLane([2, 3, 1, 2, 3, 2, 3, 3] , [[0, 3], [4, 6], [6, 7], [3, 5], [0, 7]]))