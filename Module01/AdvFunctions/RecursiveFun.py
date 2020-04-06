"""
    1. Recursive function
"""
def sum(num):
    if num == 1:
        return  1
    else:
        return sum(num - 1) + num

# Python only support depth 1000
print(sum(998))

