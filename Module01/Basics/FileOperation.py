import codecs

# 文本文件 read
f = open("test.txt", "r")
s = f.read()

# Read 2 chars
# s = f.read(2)

print(s)
f.close()

# r->read;b->binary
f = open("test.txt", "rb")
s = f.read()

# Read 2 bytes
# s = f.read(2)

print(s)
f.close()