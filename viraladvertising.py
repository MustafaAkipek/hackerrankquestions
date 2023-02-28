# int n: the day number to report

def viralAdvertising(n):
    shared = 5
    cumulative = 0
    for i in range(n):
        liked = int(shared / 2)
        cumulative += liked
        liked *= 3
        shared = liked
        
    return cumulative
        
print(viralAdvertising(5))