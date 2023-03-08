# string s: the intial string
# string t: the desired string
# int k: the exact number of operaitons that must be performed

def appendAndDelete(s, t, k):
    cs = 0
    ct = 0
    
    if len(s) < len(t):
        for i in range(len(s)):
            if s[i] == t[i]:
                cs += 1
                ct += 1
            else:
                break
    
    else:
        for i in range(len(t)):
            if s[i] == t[i]:
                cs += 1
                ct += 1
            else:
                break
                
    mneed = (len(s) - cs) + (len(t) - ct)
    

    if k > len(s) + len(t):
        return "Yes"
    
    if k >= mneed and  (k - mneed) % 2 == 0 :
        return "Yes"
    
    else:
        return "No"
    
print(appendAndDelete("hackerhappy", "hackerrank", 9))