str = 'Host: 127.0.0.1:7890'
str2 = str.split(':', 1)[1].split(':', 1)[1]
port = int(str2)
print("=====")

str3 = str.split(':')[2]
print("=====")