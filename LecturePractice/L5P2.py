
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

def recurPower(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * recurPower(base, exp - 1)

print iterPower(3, 6)
print recurPower(3, 6)