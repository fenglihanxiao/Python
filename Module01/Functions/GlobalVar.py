x = 20


def test():
    x = 10
    print(x)


def test2():
    """ Global x is been changed right here"""
    global x
    x = 10
    print(x)

test()
print("After test(), x=%d" % x)


test2()
print("After test2(), x=%d" % x)