class Circle:
    """Circle class"""
    # Variable containing a list of all circles which have been created.
    all_circles = []  # class variable
    pi = 3.14159

    def __init__(self, r=1):
        """Create a Circle with the given radius"""
        self.radius = r
        # self.__class__.all_circles.append(self)# 在instance method里解除class variable的方法示例self.__class__.pi
        Circle.all_circles.append(self)

    def area(self):
        """determine the area of the Circle"""
        return self.__class__.pi * self.radius * self.radius
        # return self.radius * self.radius * Circle.pi
#         one may object to hardcoding the name of a class inside that class’s methods. You can
# avoid doing so through use of the special __class__ attribute

    @classmethod#也多半是关系到类级别的操作才用classmethod
    def total_area(cls):
        total = 0
        for c in cls.all_circles:
            total = total + c.area()
        return total

c1 = Circle(1)
c2 = Circle(2)
print(Circle.total_area())