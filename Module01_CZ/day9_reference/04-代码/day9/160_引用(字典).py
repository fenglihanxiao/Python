"""
演示引用(字典)
"""
# print(id({}))
# print(id({}))
# print(id({"aa":1,"bb":2}))
# print(id({"aa":1,"bb":2}))

# a = {"aa":1,"bb":2}
# b = {"aa":1,"bb":2}
# print(id(a))
# print(id(b))

a = {"aa": 1, "bb": 2}
b = a
c = {"aa": 1, "bb": 2}
a["aa"] = "itcast"
print(b["aa"])
print(a)
print(b)
print(c)
