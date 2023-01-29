def dayofprogrammer(year):
    january = 31
    march = 31
    april = 30
    may = 31
    june = 30
    july = 31
    august = 31
    september = 30 
    october = 31
    november = 30
    december = 31
    
    mvp = 256
    day = 0
    month = 1
    
    
    if year > 1918: 
        if year%4 == 0 and year%100 != 0:
            february = 29
        elif year%400 == 0:
            february = 29
        else:
            february = 28
            
    elif year == 1918:
        if year%4 == 0:
            february = 29
        else:
            february = 28
        day += 13
        
    else:
        if year%4 == 0:
            february = 29
        else:
            february = 28
            
    months = [january, february, march, april, may, june, july, august, september, october, november, december]
   
    for i in range(len(months)):
        if mvp >= 28:
            mvp = mvp - months[i]
            month += 1
        else:
            day += mvp
            break
        
    if len(str(month)) < 2:
        return str(day) + ".0" + str(month) + "." + str(year)
    else:
        return str(day) + "." + str(month) + "." + str(year)

print(dayofprogrammer(1918))     
    