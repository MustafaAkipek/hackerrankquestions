# int scores[n]: points scored per game

def breakingRecords(scores):
    minimum = scores[0]
    maksimum = scores[0]
    
    minscore = 0
    maxscore = 0
    
    for i in range(1, len(scores)):
        if scores[i] < minimum:
            minscore += 1
            minimum = scores[i]
        elif scores[i] > maksimum:
            maxscore += 1
            maksimum = scores[i]
    
    return maxscore, minscore
        
print(breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]))