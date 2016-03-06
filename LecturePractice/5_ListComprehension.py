
L = [x**2 for x in range(1,7)]
print L

mixed = [1, 2,'a', 3, 4.0]
print [x**2 for x in mixed if type(x) == int]