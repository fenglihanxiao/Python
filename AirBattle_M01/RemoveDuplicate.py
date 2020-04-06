aList = [1,2,3,4,4,3,2,1,2,3,4,5,6,5,5,3,3,4,2,1]

"""
    1.  Then convert this set again to a list i.e.
"""
# aList = list(set(aList))
# print(aList)

def remove_dup(aList):
    result = []

    for i in aList:
        if i not in result:
            result.append(i)

    return result

list_re = remove_dup(aList)
print("="*50)
print("Result list=", list_re)




