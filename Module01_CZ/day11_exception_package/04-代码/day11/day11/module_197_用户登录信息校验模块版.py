"""
案例：用户登录信息校验模块版
分析：
1.异常类搬家放到独立的包中，作为模块导入使用
2.业务函数登录操作搬家放到独立的包中，作为模块导入使用
3.主程序中要使用上述模块，导入
4.所有使用模块的地方都要导入
"""

import service.service_login
from excp.question import *

name = input("请输入用户名:")
pwd = input("请输入密码:")

try:
    service.service_login.check_login(name,pwd)
except NameQuestion as e:
    print(str(e))
except PasswordQuestion as e:
    print(str(e))
else:
    print("正常登陆，请使用")




