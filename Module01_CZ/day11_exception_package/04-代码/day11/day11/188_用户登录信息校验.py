"""
案例：用户登录信息校验
要求：
    用户输入用户名，密码后对信息进行校验
    1.用户名长度在3-8个字符
    2.用户名中只能出现英文字母和数字
    3.密码长度必须是6位
    4.密码必须由纯数字组成
分析：
1.信息使用input操作获取
2.定义自定义异常，描述非法信息
3.提供检测的函数，针对情况进行处理
4.执行程序中要使用try结构完成检测
"""

class NameQuestion(Exception):
    pass
class PasswordQuestion(Exception):
    pass

def check_login(name,pwd):
    """检测用户名和密码是否合理"""
    if len(name) <3 or len(name) > 8:
        raise NameQuestion("用户名长度必须在3到8个字符之间")
    if not name.isalnum():
        raise NameQuestion("用户名中必须使用英文字母和数字组成")
    if len(pwd) != 6:
        raise PasswordQuestion("密码长度必须是6位")
    if not pwd.isnumeric():
        raise PasswordQuestion("密码必须由纯数字组成")

name = input("请输入用户名:")
pwd = input("请输入密码:")

try:
    check_login(name,pwd)
except NameQuestion as e:
    print(str(e))
except PasswordQuestion as e:
    print(str(e))
else:
    print("正常登陆，请使用")













