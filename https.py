import os
import socket
import ssl
import sys
from bcolor import bcolor

query = sys.argv[1]
head = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
headssl = ssl.wrap_socket(head)
headssl.connect_ex((sys.argv[1], 443))
headssl.sendall(f"OPTIONS / HTTP/1.1\Host:{1}".encode("utf-8"))
print(bcolor.color.OKGREEN + headssl.recv(1024))
ht = 80, 8080, 443, 8081,
#:
def __init__():
    print(bcolor.color.OKGREEN +"\t[+]HEADER[+]\n")
    arg = sys.argv[1]#input("Digite a URL => ")
    head = os.system('curl -A "Opera/9.80 (Macintosh; Intel Mac OS X; U; en) Presto/2.2.15 Version/10.00" -I {}'.format(arg))
    print(head)
