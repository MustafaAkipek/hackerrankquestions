# int k: öğrenci eşik sayısı
# int a[n] = n öğrencinin varış saatleri

# Bize verilen bilgilere bakarak eğer öğrencinin geldiği saat 0 'dan küçük ya da eşit ise bu öğrenci zamanında gelmiş demektir eğer değil ise 
# öğrenci derse geç kalmış demektir, bize verilen bir eşik değer var eğer eşik değer sayısında ya da daha fazla kişi derse zamanında gelmiş ise
# ders iptal değil ama diğer olay gerçekleşirse ders iptal demek

def angryProfessor(k, a):
    # Write your code here
    on_time = 0
    for i in a:
        if i <= 0:
            on_time +=1
        else:
            pass
            
    if on_time >= k:
        return "NO"
    else:
        return "YES"
    
a = angryProfessor(3, [5,8,2,0,-1])
print(a)