class Chinese:
    country = "China"

    def __init__(self, id_num, name):
        self.id_num = id_num
        self.name = name

    """
        1. https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
    """
    @classmethod
    def show_country(cls):
        ####################################################
        # 1. 类方法中不允许使用实例变量和实例方法
        # cls.show()
        # day4/08-面向对象.docx
        print("We are Chinese and from %s" % Chinese.country)
        c1 = cls("007", "Jame")
        cls.country = "USA"
        return c1.id_num, c1.name

    def show(self):
        print(self.name)
        ##################################################
        # Instance method can access class variables and class method
        print(Chinese.country)
        print(Chinese.show_country())
        self.print_menu()

    @staticmethod
    def print_menu():
        print("=======================")




chi = Chinese("5109", "Feng")
Chinese.show_country()
# #################################################
# # ClassName.cls_method
# Chinese.show_country()
#
# #################################################
# # instance_var.cls_method
# chi.show_country()

chi.show()

#################################
# Test for comparing

# Test for changes
chi2 = Chinese("1020", "Amy")

# Test for git add
chi3 = Chinese("1818", "Stephanie")
