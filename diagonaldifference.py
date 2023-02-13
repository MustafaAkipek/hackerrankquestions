# int arr[n][m]: an array of integers

def diagonalDifference(arr):
    leftflank = 0
    rightflank = 0
    
    n = len(arr[0])
    
    for i in range(n):
        leftflank += arr[i][i]
        rightflank += arr[i][n-1-i]
        
    return abs(leftflank - rightflank)
