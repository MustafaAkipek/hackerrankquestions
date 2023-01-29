puan = [10, 5, 20, 20, 4, 5, 2, 25, 1]

mins = 0
maks = 0

min = puan[0]
mak = puan[0]

for i in range(len(puan)):
    if puan[i] > mak:
        maks += 1
        mak = puan[i]
        
    if puan[i] < min:
        mins += 1
        min = puan[i]
        
print("Maks skor sayısı: ",maks,"Minimum skor sayısı: " ,mins)