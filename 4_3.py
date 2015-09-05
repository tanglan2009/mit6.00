def f(x):
    def g():
        x = 'abc'
        print 'x1 = ', x

    def h():
        z = x
        print 'z1 = ', z
    x = x + 1
    print 'x2 = ', x
    h()
    g()
    print 'x3 = ', x
    print "wonderful!"
    return g

x = 3
z =f(x)
print 'x = ', x
print 'z = ', z
z()