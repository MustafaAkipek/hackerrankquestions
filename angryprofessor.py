# int k: the threshold number of students
# int a[n]: the arrival times of the n students

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
    
print(angryProfessor(3, [5,8,2,0,-1]))
