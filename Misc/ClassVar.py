class Test(object):
    nums = []
    kind = 'canine'

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.inst_nums = [3, 2, 1]
        self.__private_var = "Feng"

    def add_class_item(self):
        self.nums.append(9)


    @classmethod
    def add_class_item_c(cls):
        cls.nums.append(10)


    def add_class_item02(self, i):
        self.inst_nums.append(i)

    def get_private_var(self):
        return self.__private_var


test = Test(5, 10)
test.nums.append(1)
test.nums.append(2)
test.nums.append(3)
test.kind = "cat"
test.add_class_item02(90)
print("Test.kind=", Test.kind)
print("test_instance.kind=", test.kind)
print(test.__dict__)


test2 = Test(1, 2)

test2.nums.append(4)
test2.add_class_item02(100)

# Instance method can also modify class variable
test2.add_class_item();
test.add_class_item_c();

print("=============== in obj1", test.nums, test.inst_nums)
print("=============== in obj2", test2.nums, test2.inst_nums)
print("------------ PV:%s" % test.get_private_var())
