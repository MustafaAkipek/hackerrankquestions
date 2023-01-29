#verilen dizideki elemanların toplamı istenilen sayıya bölünebilecek ya da katlarına bölünebilecek

# n ar dizisinin uzunluğu
# ar[n] = bir dizi tamsayı
# k = bölen



def divisibleSumPairs(n, k, ar):
    
    divisible = 0
    for i in range(len(ar)):
        for j in range(i+1 ,len(ar)):
            if ((ar[i] + ar[j]) % k) == 0:
                divisible += 1
    print(divisible)
            
    
    
divisibleSumPairs(6, 3, [1, 3, 2, 6, 1, 2])
