"""
演示函数形参为默认参数
"""
# def test(a = 1):
#     print(a)
#     a = 2
#     print(a)
#     print("-------------")
#
# # test(100)
# test()
# test()


# def test(a = []):
#     print(a)
#     a = [1,2,3]
#     print(a)
#     print("-------------")
#
# test()
# test()


# def test(a = []):
#     print(a)
#     a.append("itcast")
#     print(a)
#     print("-------------")
#
# test()
# test()
# test()
# test()

def test(a = []):
    print(a)
    a.append("itcast")
    print(a)
    print("-------------")

print(id(test))
print(id(test))
print(id(test))
print(id(test))