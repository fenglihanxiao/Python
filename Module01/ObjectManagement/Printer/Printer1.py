"""
    1. 172_XXX -> Case study of setting up a office Printer
"""


class Manager:
    def use_printer(self, info, pr):
        pr.add_task(info)


class Staff:
    def use_printer(self, info, pr):
        pr.add_task(info)


class Printer:
    __instance = None
    __is_init = False
    # list_print = []

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(Printer)
        return cls.__instance

    def __init__(self):
        if Printer.__is_init == False:
            print("Printer init ..................")
            self.list_print = []
            Printer.__is_init = True


    def add_task(self, info):
        """ Add info to printer's message queue """
        # Printer.list_print.append(info)
        self.list_print.append(info)

    def print(self):
        print(self.list_print)


# Programmer A:
pr1 = Printer()
mgr1 = Manager();
mgr1.use_printer("I am a Manager", pr1)
pr1.print()

# Programmer B:
pr2 = Printer()
sta1 = Staff();
sta1.use_printer("I am a Staff", pr2)
pr2.print()

printer = Printer()
printer.print()
