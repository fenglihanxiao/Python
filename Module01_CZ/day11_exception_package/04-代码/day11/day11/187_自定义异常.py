"""
演示自定义异常
"""
# name = "朱朱侠"
# if name.find("朱") >= 0 :
#     print("违规了")



# def check_name(name):
#     if name.find("朱") >= 0:
#         print("违规了")
# def check_age(age):
#     pass
#
# check_name("朱朱侠")


# def check_name(name):
#     if name.find("朱") >= 0:
#         raise ValueError("姓与国姓冲突")
#
# def check_age(age):
#     pass
#
# try:
#     check_name("朱朱侠")
#     check_age(18)
# except ValueError:
#     print("处理代码")


# 自定义异常类
class NameIsError(Exception):
    pass
class AgeIsError(Exception):
    pass
class HaHaError(Exception):
    pass

def check_name(name):
    if name.find("朱") >= 0:
        raise NameIsError("姓与国姓冲突")

try:
    check_name("朱朱侠")
except NameIsError as e:
    print(str(e))


