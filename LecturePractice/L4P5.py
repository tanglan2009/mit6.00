
def clip(lo, x, hi):
    """
    Takes in three numbers and returns a value based on the value
    of x.
    Returns:
    - lo, when x < lo
    - hi, when x > hi
    - x, otherwise
    """
    # if x < lo:
    #     return lo
    # elif x > hi:
    #     return hi
    # else:
    #     return x
    ## return min(max(x,lo), hi)
    return max(lo, min(x, hi))

print clip(3, 7, 6)