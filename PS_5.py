
# Assume that each function is tested with a list L whose elements are
# sorted in increasing order.
# assume L is a list of positive integers.

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False

def newSearch(L, e):
    size = len(L)
    for i in range(size):
        if L[size-i-1] == e:
            return True
        if L[i] < e:
            return False
    return False

#L = [1, 2, 3, 4, 5, 6, 7]
L = [3, 4]
e = 3

print search(L, e)
print newSearch(L,e)