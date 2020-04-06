"""
    1. Find hello instance
"""

def find_all(sstr, tstr):
    idx = 0
    j = 0
    res_tmp = set()
    for i in sstr:
        if j == 0:
            idx = sstr.find(tstr, j)
        else:
            idx = sstr.find(tstr, j + len(tstr))

        if idx != -1:
            # result.__add__(idx)
            res_tmp.add(idx)
        j += 1
    result = tuple(res_tmp)
    return result



str1 = "**helloc++***hellopython+++hellojava"
result = find_all(str1, "hello")
print(result)