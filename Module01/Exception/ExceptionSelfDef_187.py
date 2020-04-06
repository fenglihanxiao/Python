"""
    1. 187_XXX -> Self define exception
"""


class NameIsError(Exception):
    pass


class AgeIsError(Exception):
    pass


class HahaIsError(Exception):
    pass


def check_name(name):
    if name.find("li") >= 0:
        raise NameIsError("Collision with my king's ", name)


def check_age(age):
    if age >= 50 or age <= 18:
        raise NameIsError("Age is either too young or old.")

try:

    name = "I am feng"
    check_name(name)

    age = 19
    check_age(age)

    print(a)

except NameIsError as e:
    print(str(e))

except AgeIsError as e:
    print(str(e))

except Exception as e:
    print("---------")
    print(str(e))
