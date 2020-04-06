import re

str = """<img data-original="https://rpic.douyucdn.cn/appCovers/2016/11/13/1213973_201611131917_small.jpg"""

ret = re.search(r"https://.*?\.jpg", str)
print(ret.group())

s="This is a number 234-235-22-423"
r=re.match(r".+?(\d+-\d+-\d+-\d+)",s)
print(r.group(1))