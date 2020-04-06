import re


def main():
    while True:
        _email = input("请输入一个邮箱地址:")
        # 如果在正则表达式中需要用到了某些普通的字符，比如 . 比如? 等，仅仅需要在他们前面添加一个 反斜杠进行转义
        ret = re.match(r"([a-zA-Z_0-9]{4,20})@(163|126)\.com$", _email)
        if ret:
            print("%s符合要求...." % _email)
            print("Group=%s" % ret.group(1))
            print("Group=%s" % ret.group(2))
        else:
            print("%s不符合要求...." % _email)

if __name__ == "__main__":
    main()
