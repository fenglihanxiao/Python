b = 10

def outer():
    b = 1

    def inner():
        # b = 10
        nonlocal b
        b = b + 1  # 此时 b 变量所在的命名空间属于 local作用域
        print('inner_b is %d' % b)

    inner()
    global b
    b = 20
    print('outer_b is %d' % b)

outer()