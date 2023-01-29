def angryProfessor(k, a):
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