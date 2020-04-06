from gevent import monkey
monkey.patch_all()  # 将默认会阻塞程序的函数recv accept time.sleep变为非阻塞为了实现协程的自动切换
import socket
import re
import gevent
import sys  # sys.argv

"""
1.0 返回固定数据
2.0 返回固定网页
3.0 返回用户指定网页数据
4.0 多线程实现
5.0 多进程实现
6.0 协程实现
"""

class HTTPServer(object):
    def __init__(self, port, app):
        """初始化操作 创建属性"""
        # 创建TCP 套接字
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 设置 地址重用选项
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        # 绑定 监听
        server_socket.bind(('', port))
        server_socket.listen(128)
        # 将创建的TCP服务器套接字的引用 保存在本对象中
        self.server_socket = server_socket
        # 创建导入的模块中的app函数的引用 保存在本对象中
        self.app = app

    def start(self):
        """启动HTTPServer服务器的运行"""
        while True:
            # 接受客户端的连接
            client_socket, client_addr = self.server_socket.accept()
            print("接受到来自%s的连接请求" % str(client_addr))
            # 交给 客户端处理器进行 HTTP数据处理 以协程方式
            gevent.spawn(self.client_handler, client_socket)
            # join joinall 让主进程等待协程执行完成才会继续往下执行

    def client_handler(self, client_socket):
        # 接收用户HTTP请求报文
        recv_data = client_socket.recv(4096)
        if not recv_data:
            print("客户端断开连接")
            client_socket.close()
            return
        # print(recv_data)
        recv_str_data = recv_data.decode()
        data_list = recv_str_data.split("\r\n")
        # print(data_list)
        # GET /index.html HTTP/1.1  从请求报文的第一行 就是请求行
        request_line = data_list[0]
        result = re.match(r"\w+\s+(\S+)", request_line)
        if not result:
            print("用户请求报文错误")
            client_socket.close()
            return
        # HTTP中 资源的请求路径  /index.html  /home/python/Desktop/1.jpg
        # ./static + /index.html
        path_info = result.group(1)
        print("接收到用户的资源请求路径是%s" % path_info)

        if path_info == '/':
            path_info = '/index.html'
        # 新增功能 判断web服务器 接收的是 动态资源请求 .py
        # 还是 静态资源请求 .jpg .png .css .js
        # 伪静态 ---- .html 实际上是动态资源  - 一旦实现伪静态 .html请求将不再对应静态的html
        # 动态网页 - 含有动态资源 - 动态URL
        # 静态网页  - 只有静态资源 - 静态URL
        if path_info.endswith(".html"):
            # 动态资源处理逻辑
            env = {
                "PATH_INFO": path_info
            }
            # app函数返回就是响应体
            response_body = self.app(env, self.start_response)
            # 使用已经获取到的响应头部信息 响应体数据 拼接HTTP响应报文
            response_data = self.status_header + '\r\n' + response_body

            # 发送HTTP响应报文
            client_socket.send(response_data.encode())
            client_socket.close()
        else:
            try:
                with open("./static" + path_info, "rb") as file:
                    response_body = file.read()
            except Exception as e:
                # 给客户端回复 HTTP响应报文
                response_line = "HTTP/1.1 404 Not Found\r\n"
                response_header = "Server: PWS3.0\r\n"
                response_body = "EROOR!!!!"

                response_data = response_line + response_header + "\r\n" + response_body
                response_data = response_data.encode()
            else:
                # 给客户端回复 HTTP响应报文
                response_line = "HTTP/1.1 200 OK\r\n"
                response_header = "Server: PWS3.0\r\n"
                response_data = (response_line + response_header + "\r\n").encode('utf-8') + response_body

            finally:
                # 文本文件可以使用 二进制和文本方式读取<以文本方式读文件文件需要解码 发送需要编码>
                # 二进制文件 只能使用二进制方式读取

                # 拼接HTTP响应报文  字符串.encode() --> bytes
                client_socket.send(response_data)

                # 关闭套接字
                client_socket.close()

    def start_response(self, status, headers):
        # '200 OK', [('Content-Type', 'text/html')]
        """web服务器提供给web应用程序调用的 设置响应状态和响应头信息"""
        # 参数1 字符串类型表示状态 "200 OK"
        # 参数2 是一个存储有相应头信息的列表 里面每个元素都是一个元组(头名, 头值) 【（）（）（）（）（）】
        # self.status_header 用来存储响应头部信息(响应行 响应头)
        self.status_header = "HTTP/1.1 %s\r\n" % status
        for header_name, header_value in headers:
            self.status_header += "%s: %s\r\n" % (header_name, header_value)


def main():
    # __new__ __init__
    # print(sys.argv)
    # web.py 8080
    # HTTP服务器默认在80端口 如果浏览器请求的网址或者IP后面没有端口指定 默认请求80
    if len(sys.argv) < 3:
        print("参数格式错误 python3 web.py 8080 Application:app")
        return
    if not sys.argv[1].isdigit():
        print("参数格式错误 python3 web.py 8080 Application:app")
        return
    # ['web.py', '8888', 'Application:app']
    # print(sys.argv) 获取应用程序和app函数的名称
    module_name_app_name = sys.argv[2]
    data_list = module_name_app_name.split(":")
    # print(data_list)
    module_name = data_list[0]
    app_name = data_list[1]

    try:
        # import Application as mod
        # mod = __import__("Application")
        mod = __import__(module_name)

        # app = mod.app
        # app = getattr(mod, "app")
        app = getattr(mod, app_name)

    except Exception as e:
        return
    else:
        port = int(sys.argv[1])
        # print(port)
        http_server = HTTPServer(port, app)
        http_server.start()


if __name__ == '__main__':
    main()
    # 作业1 版本3注释
    # 作业2 使用面向对象的思想 将第六个的版本的服务器重写
    """
    吃(狗,翔) 狗.吃(翔)
    """
