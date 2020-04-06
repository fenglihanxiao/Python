"""
    1. Lambda definition
"""
# def add(a, b):
#     return  a + b

# Lambda with name
add = lambda a,b : a + b
c = add(3, 5)
print(c)

# Anonymous Lambda
result = (lambda a, b: a + b)(9, 10)
print(result)