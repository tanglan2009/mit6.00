
def iterPower(base, exp):
    """
    base: int or float.
    exp: int >= 0
    return: int or float, base ^ exp
    """
    result = 1
    while exp > 0:
        result *= base
        exp -= 1
    return result

print iterPower(3, 3)