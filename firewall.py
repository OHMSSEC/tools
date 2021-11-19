import sys

from bcolor import bcolor
from scapy.config import conf
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr

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

conf.verb = 0
#if __name__ == '__main__':
def __init__():
    print(bcolor.color.ENDC+"[!]FIREWALL[!]")
    host = sys.argv[1]
    port = [21, 22, 23, 25, 53, 80, 81, 88, 110, 111, 113, 135, 139, 143, 443, 445, 465, 514, 990, 993, 995, 1025,
            1027, 1433, 1723, 3306, 3389, 5432, 5900, 6001, 8080, 8081, 10000]  # '''lista top portas de serviços'''
    packet = IP(dst=host) / TCP(sport=53, dport=port, flags="S")  # '''ip de destino recebe host e a port e envia uma flag syn'''
    ans, unans = sr(packet, inter=0.1, timeout=1)  # '''recebe um pacote com 1s de resposta'''
    head = '|PORT| - |STATE|'
    print("{}".format(head))
    for packetrecv in ans:
        if packetrecv[1].haslayer("ICMP"):  # '''pacote icmp 1 open o drop reject'''
            if packetrecv[1]["ICMP"].type == 3 \
                    and packetrecv[1]["ICMP"].code == 3:
                print (packetrecv[0]["TCP"].dport, "| [REJECT]")
        elif packetrecv[1].haslayer("TCP"):
            print (packetrecv[1]["TCP"].sport, "\t|",
                   packetrecv[1]["TCP"].sprintf("[%flags%] "))  # ''' printa as flags sa ra'''
    for packetnotrecv in unans:
        print (packetnotrecv.dport, "| [DROP]")

# for port in [21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 445, 993, 995, 1723, 3306, 3389, 5900, 8080, ]:

# 204.79.197.203
