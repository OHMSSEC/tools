# coding=utf-8
import socket
import os
import sys
import pyfiglet
VERMELHO = '\033[31m'
HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[32m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'


ascii_banner = pyfiglet.figlet_format("P-RECON")
print(ascii_banner)

print(' --------banner grabbing-------')
print(' V-0.1 by Pretilso')
print('+' * 40)

query = b'\r\n'
if sys.argv[1] == 0:
    print('Usage : python pscan.py [host/ip]')


if sys.argv[1] != float:
    ip = socket.gethostbyname(sys.argv[1])  # Convert url to ip
else:
    s_old = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_old.connect(("whois.iana.org", 43))
    s_old.send(sys.argv[1] + query)
    resp = s_old.recv(1024).split()
    correct = (resp[19])

    s_new = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s_new.connect_ex((correct, 43))
    s_new.send(sys.argv[1] + query)
    response = s_new.recv(1024)
    print(response)

print('+' * 40)

os.system("curl " + sys.argv[1] + " -I")
print('+' * 40)
os.system("host -t cname " + sys.argv[1])
print('+' * 40)

for port in [20, 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, ]:
    s_future = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    if s_future.connect_ex((sys.argv[1], port)) == 0:
        banner = s_future.recv(1024)
        print('\033[32m'"[PORT] [OPEN] " + WARNING + " | {} |  | {} |".format(port, banner))

    else:
        print(FAIL + "[PORT]  [CLOSE/DROP/FILTERED]|{}|".format(port))
