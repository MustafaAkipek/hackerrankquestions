def hesapla():
    notlar = [35,55,69]

    for i in range(len(notlar)):
        if notlar[i] > 37 and notlar[i] % 5 != 0 and (notlar[i] % 5) > 2:
            notlar[i] += 5 - (notlar[i] % 5)
    return notlar

print(hesapla())
