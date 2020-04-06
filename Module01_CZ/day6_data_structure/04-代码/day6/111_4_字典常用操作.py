"""
演示字典常用操作
"""
dict1 = {"name":"大帅","age":20}

dict1["name1"] = "小帅"
print(dict1)
print(dict1.get("name2"))
# print(dict1["name2"])

print(dict1.keys())
print(dict1.values())
print(dict1.items())