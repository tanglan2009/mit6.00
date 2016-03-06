
def recurPower(base, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return base
    return base * recurPower(base, exp - 1)

def recurPowerNew(base, exp):
    if exp <= 0:
        return 1
    if exp%2 == 0:
        return recurPowerNew(base*base, exp/2)
    else:
        return base*recurPowerNew(base, exp - 1)

print recurPowerNew(2,6)