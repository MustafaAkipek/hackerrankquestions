

#Girilen notların duruma göre yuvarlanması
#eğer sayımız 37 'dün küçük ise karışılmayacak
#5 'e göre modu 0 'a eşit ise karışılmayacak
#5 'e göre modu 2 'den büyük ise 5 'in katına tamamlanacak

def hesapla():
    notlar = [35,55,69]

    for i in range(len(notlar)):
        if notlar[i] > 37 and notlar[i] % 5 != 0 and (notlar[i] % 5) > 2:
            notlar[i] += 5 - (notlar[i] % 5)
    return notlar

print(hesapla())
