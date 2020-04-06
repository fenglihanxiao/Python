"""
演示字典参数应用
"""
"""流水线作业一"""
# 要求：两端去空格，小写转大写，按照空格切割字符串，输出字符串，同行输出，间隔使用：
# "  hello itcast python  " -> HELLO:ITCAST:PYTHON:
# def coder1(str):
#     # 对数据进行处理
#     str_list = str.split()
#     return str_list
# def coder2(str):
#     # 对数据进行处理
#     # 交由下一流水线继续作业
#     new_str = str.strip()
#     new_str = new_str.upper()
#     return coder1(new_str)
# # 提供数据，指定最终处理策略
# str_list = coder2("  hello itcast python  ")
# for data in str_list:
#     print(data ,end=": ")

"""流水线作业二"""
# def coder1(str):
#     # 对数据进行处理
#     str_list = str.split()
#     for data in str_list:
#         print(data, end=",")
# def coder2(str):
#     # 对数据进行处理
#     # 交由下一流水线继续作业
#     new_str = str.strip()
#     new_str = new_str.upper()
#     return coder1(new_str)
# # 提供数据，指定最终处理策略
# coder2("  hello itcast python  ")

"""流水线作业三"""
# def coder1(str,end):
#     # 对数据进行处理
#     str_list = str.split()
#     for data in str_list:
#         print(data, end=end)
# def coder2(str,end):
#     # 对数据进行处理
#     # 交由下一流水线继续作业
#     new_str = str.strip()
#     new_str = new_str.upper()
#     return coder1(new_str,end)
# # 提供数据，指定最终处理策略
# coder2("  hello itcast python  ","-")

"""流水线作业四"""
def coder1(str,**kwargs):
    # 对数据进行处理
    str_list = str.split()
    for data in str_list:
        print(data,**kwargs)

def coder2(str,**kwargs):
    # 对数据进行处理
    # 交由下一流水线继续作业
    new_str = str.strip()
    new_str = new_str.upper()
    return coder1(new_str,**kwargs)

# 提供数据，指定最终处理策略
coder2("  hello itcast python  ",end="%")
print("*" * 20)


def call_depth_4( d =10 ,**kwargs):#   d中 d 留
    print("call_depth_4,d = %d" % d)

def call_depth_3( c =10,**kwargs): #  cd中 c 留，d 使用字典参数向后传递
    print("call_depth_3,c = %d" % c)
    call_depth_4(**kwargs)

def call_depth_2( b =10,**kwargs ): # bcd中 b 留，cd 使用字典参数向后传递
    print("call_depth_2,b = %d" % b)
    call_depth_3(**kwargs)

def call_depth_1( a =10 ,**kwargs): #abcd中 a 留，bcd 使用字典参数向后传递
    print("call_depth_1,a = %d" % a)
    call_depth_2(**kwargs)

call_depth_1(a = 1,b = 2,c = 3,d =4)






