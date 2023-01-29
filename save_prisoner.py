#mahkum sayımız var, şeker sayımız var, sandalyenin başlayacağı numaramız var
#şekerler dağıtılmaya başlarsa hangi mahkumda biter

# n = mahkum sayısı
# m = şeker sayısı
# s = sandalyenin başlayacağı numara



def saveTheProisoner(n, m, s):
    liste = [i for i in range(1,n+1)]   #kişi numaralarını bir liste içinde oluşturduk
    m = m % n   # şeker sayısının mahkum sayısına göre modunu aldık ki attığı turlarda zatn başa döneceği için boşuna uğraşmayalım
    while m != 0:  # şeker sayımız 0 'a eşit değilse devam et
        s += 1   #kişi numarasını 1 arttır
        m -= 1   #şeker sayısını 1 azalt
    print(liste[s-2])      #şekeri ilk numaralı kişiye dağıtmadığımız -1 ordan diğer -1 ise indis kullandığımızdan dolayı 1 daha çıkardık
    
saveTheProisoner(3, 7, 3)