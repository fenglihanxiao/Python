"""
案例：判断用户输入的用户名是否合法
    用户名通过键盘输入
    满足以下规则为合法用户名
    长度在3-8位之间
(新需求)由字母和数字组成
(新需求)首字符不是数字
"""
name = input("请输入用户名：")
if len(name)>=3 and len(name)<=8 and ????:
    print("用户名合法")
else:
    print("用户名非法")