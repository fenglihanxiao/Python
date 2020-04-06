"""
    1. strip
    2. lstrip
"""
str = "***hello*world***"
print(str.strip("*"))
print(str.lstrip("*"))

############################################
# 1. default strip is white space
str2 = "  hello*world   "
print(str2.strip())
print(str2.lstrip())

"""
    1. ljust
    2. rjust
"""
str = "itcast"
print(str.ljust(8, "*"))
print(str.rjust(8, "*"))
print(str.center(9, "*"))