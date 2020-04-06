def jiacu(func_1):
    print('----加粗----')

    def inner_1():
        return '--加粗--' + func_1() + '--加粗--'

    return inner_1


def xieti(func_2):
    print('---斜体---')

    def inner_2():
        return '--斜体--' + func_2() + '--斜体--'

    return inner_2


@jiacu  # test3 = jiacu(test3)
@xieti  # test3 = xieti(test3) = inner_2   #先执行 这个语句，然后才会执行 @jiacu
def test3():
    return 'hello world--3'


if __name__ == '__main__':
    re = test3()
    print(re)