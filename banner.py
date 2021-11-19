
import socket
import sys
from bcolor import bcolor
import time
from tqdm import tqdm

i = [21, 22, 23, 25, 53, 88, 110, 111, 113, 135, 139, 143, 445, 465, 514, 990, 993, 995, 1025,
     1027, 1433, 1723, 3306, 3389, 5432, 5900, 6001, 10000]
n = [21, 22, 23, 25, 53, 88, 110, 111, 113, 135, 139, 143, 445, 465, 514, 990, 993, 995, 1025,
     1027, 1433, 1723, 3306, 3389, 5432, 5900, 6001, 10000]


# i = [1234]

def __init__():
    try:
        print(bcolor.color.OKGREEN + "\t[+]HEADER[+]\nCURL USE:")


        for port in i:
            s_future = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            if s_future.connect_ex((sys.argv[1], port)) == 0:
                banner = s_future.recv(2048)
                print(bcolor.color.OKGREEN + "[PORT] [OPEN] "  " | {} |  | {} |".format(port, banner))

            else:
                print(bcolor.color.FAIL + "[PORT]  [CLOSE/DROP/FILTERED]|{}|".format(port))
        for port in tqdm(range(100)):
            time.sleep(0.1)

        tqdm.write(bcolor.color.OKGREEN + "[!]CONCLUIDO[!]")
    except KeyboardInterrupt:
        print(bcolor.color.WARNING + "[!] O PROGRAMA FOI ENCERRADO")
        sys.exit()
