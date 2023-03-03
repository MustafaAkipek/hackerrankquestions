# string s: a time in 12 hour format

def timeconversion(s):
    hour = s.split(":")
    
    if s[-2:] == "PM" and int(hour[0]) < 12:
        hour[0] = str(int(hour[0]) + 12)
        
    if s[-2:] == "AM" and int(hour[0]) > 12:
        hour[0] = str(int(hour[0]) - 12)
        
    if s[-2:] == "AM" and int(hour[0]) == 12:
        hour[0] = "00"
 
    newhour = ":".join(hour)
    return newhour[:8]
    
print(timeconversion("07:05:45PM"))