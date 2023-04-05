# int b: the number of black gifts
# int w: the number of white gifts
# int bc: the cost of a black gift
# int wc: the cost of a white gift
# int z: the cost to convert one color gift to the other color

def taumBday(b, w, bc, wc, z):
    cost = 0
    if bc < wc:
        cost += bc * b
        if bc + z < wc:
            cost += w * (bc + z)
        else:
            cost += wc * w

    else:
        cost += wc * w
        if wc + z < bc:
            cost += b * (wc + z)
        else:
            cost += bc * b

    return cost

print(taumBday(3,3, 1, 9, 2))