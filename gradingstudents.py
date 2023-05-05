# int[n]: the grades after rounding as appropriate

def gradingStudents(grades):
    nresult = []
    
    for i in grades:
        if i > 37 and (i % 5) > 2:
            i += 5 - (i % 5)
        nresult.append(i)

    return nresult   
 
print(gradingStudents([73, 67, 38, 33]))
