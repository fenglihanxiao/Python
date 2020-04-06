def set_func(func):
    print("============= set_func ==============")
    def call_func():
        print("---这是权限验证1----")
        print("---这是权限验证2----")
        func()

    return call_func


@set_func #
def test1():
    print("-----test1----")


test1()


# foo = lambda x: x + 1
#
# val = foo()
#
# print("val=%d" % val)