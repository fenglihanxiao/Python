"""
演示异常处理机制
"""
# def oper1():
#     print( 1 / 0 )
#
# def oper2():
#     oper1()
#
# def oper3():
#     oper2()
#
# try:
#     oper3()
# except:
#     print("处理")

# def oper1():
#     print( 1 / 0 )
#
# def oper2():
#     try:
#         oper1()
#     except:
#         print("处理掉")
#
# def oper3():
#     oper2()
#
# oper3()


try:
    try:
        a = 1
        print(a)
        b = 1/0
    except NameError:
        print("名称处理完毕")
except ZeroDivisionError:
    print("0的处理完毕")







