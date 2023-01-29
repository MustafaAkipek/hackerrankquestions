def getMoneySpent(keyboards, drives, b):
    makspend = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b:
                makspend.append(keyboards[i] + drives[j])
                
    
    if len(makspend) != 0:
        mak = makspend[0]
        for i in range(len(makspend)):
            if makspend[i] <= b and makspend[i] > mak:
                mak = makspend[i]
        return mak
    else:
        return -1       
        

print(getMoneySpent([40,50,60], [5,10,12], 60))
