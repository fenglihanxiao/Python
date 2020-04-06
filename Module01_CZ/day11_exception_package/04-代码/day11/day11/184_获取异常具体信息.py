"""
演示捕获具体异常信息
"""
try:
    b = 1/0
except ZeroDivisionError as error:
    print("发现了除法错误：" + str(error))
