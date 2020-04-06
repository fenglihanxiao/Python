import socket


def main():
    # 创建一个udp套接字

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    ip_addr = input("Please enter IP Address:")
    port = int(input("Please enter Port Number:"))

    # 从键盘获取数据
    send_data = input("请输入要发送的数据：")

    # 可以使用套接字收发数据
    # udp_socket.sendto("hahahah", 对方的ip以及port)
    # udp_socket.sendto(b"hahahah------1----", ("192.168.33.53", 8080))
    udp_socket.sendto(send_data.encode("utf-8"), (ip_addr, port))

    recv_data = udp_socket.recvfrom(1024)

    print(recv_data)

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
