# int k: the height the character can jump naturally
# int height[n]: the heights of each hurdle

def hurdleRace(k, height):
    peak = max(height)
    if k >= peak:
        return 0
    else:
        return peak - k

print(hurdleRace(1, [1,2,3,3,2]))