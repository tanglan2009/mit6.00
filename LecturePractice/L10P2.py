def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def search(L, e):
    for i in L:
        if i == e:
            return True
        if i > e:
            return False
    return False

def search2(L, e):
    for i in L:
        if i == e:
            return True
        elif i > e:
            return False
    return False

def search3(L, e):
    if L[0] == e:
        return True
    elif L[0] > e:
        return False
    else:
        return search3(L[1:], e)

def search4(L, e):
    if len(L) <= 0:
        return False
    else:
        if L[0] == e:
            return True
        elif L[0] > e:
            return False
        else:
            return search4(L[1:], e)















