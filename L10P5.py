
def selSort(L):
    for i in range(len(L) - 1):
        minIndx = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal = L[j]
            j += 1
        if minIndx != i:
            temp = L[i]
            L[i] = L[minIndx]
            L[minIndx] = temp
    return L

def newSort(L):
    for i in range(len(L) - 1):
        j = i + 1
        while j < len(L):
            if L[i] > L[j]:
                temp = L[i]
                L[i] = L[j]
                L[i] = temp
            j += 1
    return L


L = [0, 2, 1, 6, 4]
print selSort(L)
print newSort(L)