import os
import socket
from datetime import datetime


def server(local, port):
    """Server honey or backd """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind((local, port))
        s.listen(1)
        print(f"[+]Escutando ...  {s.getsockname()}\t{datetime.today().strftime('%A, %B %d, %Y %H:%M:%S')}")
        cmd = {'HELP': '--help'}
        while True:

            conn, addr = s.accept()
            print(f"[+]Conectado S/ACK | {addr}")

            conn.sendall(b'\r\n220 Welcome to Cerberus FTP Server 5.0.1.2\r\n')

            # conn.sendall(b"200 Apache Tomcat v-2.3.5b")

            data = conn.recv(8192)
            conn.shutdown(socket.SHUT_WR)

            print(f"[+]Bytes recebidos  {len(data)}  | {conn.getpeername()}  ")
            print(f"[+]Bytes decode  {data.decode('ascii', 'ignore')} | {conn.getpeername()}")

            log = data.decode('ascii', 'ignore')  # salvar em arquivo de texto

            # os.system(f'{data.decode("ascii")}')
            if conn.close():
                os.popen("tome uma aç~ao ")




    except KeyboardInterrupt:
        print("[!]Servidor Interrompido[!]")


# OSError: [Errno 98] Address already in use - aguarde


server('192.168.0.106', 21)
