"""
    1. 166_XXX
"""

# def test(a=1):
#     print(a)
#     a = 2
#     print(a)
#     print("==================")
#
# test()
# test()

"""
    2. 
"""


# def test(a = []):
#     print(a)
#     a = [1, 2, 3]
#     print(a)
#     print("==================")
#
# test()
# test()

"""
    =====================================================================
    3. second time call test(), a's reference address does not change
       but the reference address which point to physical address is been modified
       by first function call
    =====================================================================
"""
def test(a = []):
    print(a)
    # first function call and second function call has the same reference address
    print("********", id(a))
    a.append("itcast")
    print(a)
    print("==================")

test()
test()

###############################################
# id is different excersi
lst = []
print(id(lst))
lst.append("feng")
lst = []
print(id(lst))
lst.append("li")
print(lst)