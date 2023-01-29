# bir dizi de elemanlar veriliyor ve pozitif, negatif, nötr sayılardan kaç tane var ise ayrı ayrı hesaplıyoruz
# sonrasında ise toplam eleman sayısına bölüyoruz, ama virgülden sonra 6 basamak olmalı

# arr bize verilen dizi

a = [1, 1, 0, -1, -1]

def plusMinus(a):
    presult = 0
    nresult = 0
    zeron = 0
    
    for i in range(0,5):
        if a[i] > 0:
            presult += 1
        if a[i] == 0:
            zeron += 1
        if a[i] < 0:
            nresult += 1
            
    positiveration = presult/len(a)
    negativeration = nresult/len(a)
    zeroration = zeron/len(a) 
       
    return f"{positiveration:.6f}\n{negativeration:.6f}\n{zeroration:.6f}"
    
            


print(plusMinus(a))