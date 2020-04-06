"""
    1. https://stackoverflow.com/questions/12179271/meaning-of-classmethod-and-staticmethod-for-beginner
"""

class Chinese:
    country = "China"

    def __init__(self, id_num, name):
        self.__id_num = id_num
        self.__name = name

    @staticmethod
    def show():
        print("Today is good wheather")
        print("Access class variable in static method", Chinese.country)


chi = Chinese("5109", "Feng")
chi.show()
Chinese.show()