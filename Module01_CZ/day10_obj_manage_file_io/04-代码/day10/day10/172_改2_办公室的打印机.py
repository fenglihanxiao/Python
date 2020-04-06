"""
案例：办公室的打印机
一台打印机可以服务于一个办公室中所有的人，完成他们的打印任务。
分析：
1.打印机：将要打印的任务添加到打印的任务队列中，真正的打印操作
2.经理：将要打印的操作加入打印机中
3.员工：将要打印的操作加入打印机中
"""
class Manager:
    def use_printer(self,info,pr):
        pr.add_task(info)

class Staff:
    def use_printer(self,info,pr):
        pr.add_task(info)

class Printer:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None :
            cls.__instance = object.__new__(Printer)
        return cls.__instance

    def __init__(self,list_print = []):
        self.list_print = list_print

    def add_task(self,info):
        """添加打印信息到打印队列中"""
        self.list_print.append(info)

    def print(self):
        print(self.list_print)

# 程序员A：
pr1 = Printer()
m1 = Manager()
m1.use_printer("hello",pr1)

# 程序员B：
pr2 = Printer()
st1 = Staff()
st1.use_printer("itcast",pr2)

# 程序员B1：
pr3 = Printer()
st2 = Staff()
st2.use_printer("itcast666",pr3)

# 程序员C：
pr = Printer()
pr.print()
