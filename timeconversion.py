# string s: a time in 12 hour format

def timeconversion(s):
    time = s.split(":") # ["07","05","45PM"]
    
    if s[-2:] == "PM" and int(time[0]) < 12:
        time[0] = str(int(time[0]) + 12)
    
    if s[-2:] == "AM" and int(time[0]) > 12:
        time[0] = str(int(time[0]) - 12)
        
    if s[-2:] == "AM" and int(time[0]) == 12:
        time[0] = "00"
        
    ntime = ":".join(time) # 19:05:45PM
    return str(ntime[:-2])
    
print(timeconversion("07:05:45PM"))