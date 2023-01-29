#bir dizi verilecek
#dizinin ilk değeri hem min değer hemde maks değer olucak
#eğer ki maks değer iken yeni yapılan sayı maks değerden büyük ise mak 1 artacak 
#eper ki min değer iken yeni yapılan sayı min değerden daha küçük ise min 1 artacak
#en sonra ise min ve maks yazdırılacak

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