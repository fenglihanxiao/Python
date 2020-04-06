class Chinese:
    country = "China"

    def __init__(self, id_num, name):
        self.__id_num = id_num
        self.__name = name

    ###############################################
    # Normal way to define instance method
    #   1. self is interpreter out fill for self(this) pointer
    # def show(self):
    #     print(self.__name)

    ###############################################
    # Still define instance method
    # Be cautious of this trap
    def show(cls):
        print(cls.__name)


chi = Chinese("5109", "Feng")
chi.show()