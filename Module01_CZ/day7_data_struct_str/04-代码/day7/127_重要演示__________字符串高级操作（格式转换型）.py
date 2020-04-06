"""
案例：判断用户输入的用户名是否合法
    用户名通过键盘输入
(新需求)兼容用户输入的信息前后可能带有空格
    满足以下规则为合法用户名
    由字母和数字组成
    首字符不是数字
    长度在3-8位之间

"""
name = input("请输入用户名：")
# 做用户输出信息包含空格的信息处理
name = ???
first_letter = name[0]
if len(name)>=3 and len(name)<=8 and not first_letter.isdigit() and name.isalnum():
    print("用户名合法")
else:
    print("用户名非法")




