"""
演示捕获具体异常
"""
try:
    # a = "python"
    print(a)
    print(a.index("o"))
    b = 1 / 0
except NameError:
    print("变量a没有被定义，请定义后使用")
except ValueError:
    print("被查询的内容没有找到")
except Exception:
    print("未知的异常")



