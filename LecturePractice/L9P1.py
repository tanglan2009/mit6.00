def linearSearch(L, x):
    for e in L:
        if e == x:
            return True
    return False

print linearSearch([20, 10, 1, 7, 4, 22, 25, 12, 31], 26)