# int h: the hour of the day
# int m: the minutes after the hour

def timeInWords(h, m):
    time = {1: "one", 
            2: "two", 
            3: "three", 
            4: "four", 
            5: "five", 
            6: "six", 
            7: "seven", 
            8: "eight", 
            9: "nine", 
            10: "ten", 
            11: "eleven", 
            12: "twelve", 
            13: "thirteen",
            14: "fourteen",
            15: "quarter", 
            16: "sixteen", 
            17: "seventeen", 
            18: "eighteen",
            19: "nineteen", 
            20: "twenty", 
            21: "twenty one",
            22: "twenty two",
            23: "twenty three",
            24: "twenty four",
            25: "twenty five",
            26: "twenty six",
            27: "twenty seven",
            28: "twenty eight",
            29: "twenty nine"}
    
    if m == 0:
        return time[h] + " o' clock"
    
    elif m == 1:
        return time[m] + " minute past " + time[h]
    
    elif m == 15:
        return "quarter past " + time[h]
    
    elif m == 30:
        return "half past " + time[h]
    
    elif m > 30:
        h += 1
        m = 60 - m
        if m == 15:
            return "quarter to " + time[h]
        else:
            return time[m] + " minutes to " + time[h]
        
    else:
        return time[m] + " minutes past " + time[h]

print(timeInWords(5,1))