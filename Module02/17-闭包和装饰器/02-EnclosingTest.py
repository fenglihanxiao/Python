x = 300


def test01():
    x = 200

    def test02():
        nonlocal x
        print("=============== x=%d" % x)
        x = 100
        print("=============== x=%d" % x)
    return test02

t1 = test01()
t1()
print("Global x=%d" % x)
