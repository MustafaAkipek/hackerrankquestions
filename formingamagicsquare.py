# int s[3][3]: a 3x3 array of integers

import sys

def getCost(square, s):
    cost = 0
    for i in range(3):
        for j in range(3):
            cost += abs(square[i][j] - s[i][j])
    return cost

def formingMagicSquare(s):
    all_magic = [
        [[8,1,6],[3,5,7],[4,9,2]],
        [[2,9,4],[7,5,3],[6,1,8]],
        [[6,1,8],[7,5,3],[2,9,4]],
        [[4,9,2],[3,5,7],[8,1,6]],

        [[6,7,2],[1,5,9],[8,3,4]],
        [[4,3,8],[9,5,1],[2,7,6]],
        [[8,3,4],[1,5,9],[6,7,2]],
        [[2,7,6],[9,5,1],[4,3,8]],
    ]
    
    minCost = sys.maxsize
    
    for square in all_magic:
        cost = getCost(square, s)
        minCost = min(minCost, cost)
    
    return minCost
        
print(formingMagicSquare([
                            [5,3,4],
                            [1,5,8],
                            [6,4,2]
                                    ]))

"""
    
"""