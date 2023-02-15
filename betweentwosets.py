# int a[n]: an array of integers
# int b[m]: an array of integers

def getTotal(a, b):
   factors_a = []
   factors_b = []
   common_factors = []
   max_len = len(a + b)
   
   for i in range(1, 101):
      for number in a:
         if i % number == 0:
            factors_a.append(i) 
   
   for i in range(1,101):
      for number in b:
         if number % i == 0:
            factors_b.append(i)
            
   union_list = factors_a + factors_b
   
   for number in union_list:
      if union_list.count(number) == max_len:
         common_factors.append(number)
         
   return len(set(common_factors))
   
print(getTotal([2,6],[24,36]))