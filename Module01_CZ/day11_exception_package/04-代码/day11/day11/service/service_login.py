from excp.question import *
def check_login(name,pwd):
    if len(name) <3 or len(name) > 8:
        raise NameQuestion("用户名长度必须在3到8个字符之间")
    if not name.isalnum():
        raise NameQuestion("用户名中必须使用英文字母和数字组成")
    if len(pwd) != 6:
        raise PasswordQuestion("密码长度必须是6位")
    if not pwd.isnumeric():
        raise PasswordQuestion("密码必须由纯数字组成")