# def add(a, b):
#     return  a + b

# Lambda with name
# add = lambda a,b : a + b
# c = add(3, 5)
# print(c)
#
# # Anonymous Lambda
# result = (lambda a,b : a + b)(9, 10)
# print(result)

"""
    1. Lambda definition no parameters
"""
f1 = (lambda : 100)()
print(f1)

"""
    1. Lambda return tuple
    2. TypeError: 'tuple' object is not callable
"""
# f2, f3 = (lambda: 3, 4)()

# tuple can be packed by our developer
f2, f3 = (lambda: (3, 4))()
print(f2, f3, sep="|")

"""
    1. Lambda no return value is not applicable.
    2. regular function with out explicit retrun -> return None 
"""
f4 = (lambda: print("itcast"))()
print(f4)

# tuple can be packed by our developer
f4 = (lambda: (print("itcast"), print("cool new york")))()
print(f4)

"""
    1. Lambda store data structure
"""
f5 =(lambda : [1, 2, 3])()
print(f5)

f6 =(lambda: [i for i in range(1, 101) if i % 2 == 0 and i % 7 ==0])()
print(f6)