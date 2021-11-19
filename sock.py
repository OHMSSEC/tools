import socket
import sys


def top_1(host):
    """ Simple scan obtem o banner """
    global port

    for port in [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 3306]:
        s_future = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        if s_future.connect_ex((host, port)) == 0:
            s_future.send(b'', 4)  # [PSH,ACK]
            banner = s_future.recv(1024)  # [ACK]
            s_future.sendall(b'HELP')
            print(
                '\033[32m'f"[PORT]  [OPEN]    | {port} | {socket.getservbyport(port).upper()} | {banner} |")  # [HANDSHAK]
            # [FIN,ACK]
        else:
            print('\033[1;31m'f"[PORT]  [CLOSE/DROP/FILTERED] | {port} | {socket.getservbyport(port).upper()} |")


# [RST,ACK]


top_1('192.168.0.106')


def custom(host, ports):
    for i in range(ports):
        try:
            c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if c.connect_ex((host, i)) == 0:

                flag = c.recv(1024)
                print(f"{i}  | {socket.getservbyport(i)} | {flag} |")
            else:
                print(f"{i} | {socket.getservbyport(i)} | ")
        except OSError:
            pass
# custom('192.168.0.106', 80)
