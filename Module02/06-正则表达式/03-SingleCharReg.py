import re

str = "fengli891"

# str = "02812345678"

# str = "abcd\nnm\nav"

# 匹配单词字符，即a - z、A - Z、0 - 9、_
# ret = re.match(r"fengli\w", str)

# ret = re.match(r"fengli\s\d", str)

# ret = re.match(r"fengli\W", str)

# ret = re.match(r"\s*fengli\s*", str)

ret = re.match(r"fengli\d{1,2}$", str)

# ret = re.match(r"028-?12345678", str)

# re.S indicates include /n
# ret = re.match(r".*", str, re.S)

if ret:
    print("The %s is matched by pattern %s" % (str, ret.group()))
else:
    print("Pattern does not match")