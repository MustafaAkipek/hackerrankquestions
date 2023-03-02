# int a[n]: an array of integers
# int b[m]: an array of integers

def getTotal(a, b):
   alist = []
   blist = []
   unionl = []
   common = []
   maxlen = len(a+b)
   
   for i in range(len(a)):
      start = 0
      while start < min(b):
         start += a[i]
         alist.append(start)
         
   for i in range(len(b)):
      for j in range(b[i],0,-1):
         if b[i] % j == 0:
            blist.append(j)  
            
   unionl = alist + blist
    
   for number in unionl:
      if unionl.count(number) == maxlen:
         common.append(number)
         
   return len(set(common))        
   
print(getTotal([2,6],[24,36]))