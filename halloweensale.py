# int p: the price of the first game
# int d: the discount from the previous game price
# int m: the minimum cost of a game
# int s: the starting budget

def howManyGames(p, d, m, s):
    piece = 0

    while(s >= p):
        piece += 1
        s -= p
        
        if p >= m and p-d >= m:
            p -= d
        else:
            p = m

    return piece

print(howManyGames(73, 72, 44, 9163))