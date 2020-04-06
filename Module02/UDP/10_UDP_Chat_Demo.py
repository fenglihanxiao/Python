import socket



def send_msg(udp_socket):
    """ Send message """
    dest_ip = input("Please enter destination IP Address:")
    dest_port = int(input("Please enter Port Number:"))
    send_data = input("Please enter the message:")

    udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """ Receive Message """
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data)
    print("%s:%s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # bind IP and port
    udp_socket.bind(("", 41321))

    while True:
        print("================== Welcome to UDP Chat Room ===================")
        print("[1] Send message")
        print("[2] Receive message")
        print("[0] Exit from system")
        choice = input("Please enter your choice:")

        if choice == "1":
            send_msg(udp_socket)
        elif choice == "2":
            recv_msg(udp_socket)
        elif choice == "0":
            break

if __name__ == "__main__":
    main()