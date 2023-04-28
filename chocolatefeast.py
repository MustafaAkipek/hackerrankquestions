# int n: Bobby's initial amount of money
# int c: the cost of a chocolate bar
# int m: the number of wrappers he can turn in for a free bar

def chocolateFeast(n, c, m):
    chocolate = n // c
    wrapper = chocolate

    while(wrapper >= m):
        chocolate += 1
        wrapper += 1
        wrapper -= m

    return chocolate
    
print(chocolateFeast(15, 3, 2))