import ctypes
import os
import re
import socket
import sys
from bcolor import bcolor
import time
from random import choice

import banner
import bs4
import dns.zone
import dns.resolver
import pyfiglet as pyfiglet
import requests
import bar
import firewall
import https
from tqdm import tqdm

class B_color:
    def __init__(self):
        pass

    OKRED = '\033[31m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[32m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


B_color()
kernel32 = ctypes.windll.kernel32
kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
# habilitar suporte para cor teminal windowns ansii
''':authority: who.is
:method: GET
:path: /whois-ip/ip-address/177.27.239.247
:scheme: https
52.203.44.235:443'''
if __name__ == '__main__':
    ascii_banner = pyfiglet.figlet_format("\t\t[+]LIMBO-R[+]\t".upper())
    print(bcolor.color.WARNING + ascii_banner)
    print(bcolor.color.BOLD + "\t\t\tBY - PRETILSO\n")


def bar():
    for i in tqdm(range(100)):
        time.sleep(0.1)
    tqdm.write(bcolor.color.OKGREEN + "[!]CONCLUIDO[!]")


print('\t\t[+] DNS = Resolving . . .\n')

time.sleep(5), '\n'

for regexs in 'A', 'AAAA', 'CNAME', 'MX', 'NS', 'PTR', 'TXT', 'SOA', 'HINFO':  # cname alias possivel subdomain take
    # over
    resp = dns.resolver.query(sys.argv[1], regexs, raise_on_no_answer=False)  # lib resolve

    if resp.rrset is not None:
        out = (str(resp.rrset))
        print(out)
# http://businesscorp.com.br/
# www.kuponya.com.br
# bar.__init__()
# word = ['web', 'webmail', 'infra', 'dev', 'intranet', 'net', 'adm', 'ftp', 'www', 'ns0', 'ns1', 'ns2', 'ns3',
# 'server', 'root']

print('\t\t[+] BRUTE FORCE = INIT ...\n')  # brute force add  encontrar possiveis cnames
bar()
domain = sys.argv[1]  # input('Informe o (NXDOMAIN) =>')
with open("wordlist.txt") as arquivo:
    wordl = arquivo.readlines()
for word in wordl:
    force = word.strip("\n") + "" + domain
    try:
        print(force + ":" + socket.gethostbyname(force))
    except socket.gaierror:
        pass
    '''for force in 'CNAME':
        cn = dns.resolver.query(domain, force, raise_on_no_answer=False)
        if cn.rrset is not None:
            outp =(str(cn.rrset))
            print(outp)'''
# UnicodeError: label empty or too long
bar()
print('\t\t[+] TRZ = ZONE TRANSFER . . .\n')  # atenção ao registro spf possivel mailspoofing
try:
    ns = sys.argv[1]  # input("Informe o NS => ")

    time.sleep(5), '\n'

    registroNS = dns.resolver.query(ns, 'NS')
    # tranferencia de zona
    lista = []
    for registro in registroNS:
        lista.append(str(registro))

    for registro in lista:
        try:

            trzf = dns.zone.from_xfr(dns.query.xfr(registro, ns))
        except dns.resolver.NXDOMAIN:
            print(bcolor.color.FAIL + "(NXDOMAIN)NS  não permitido tente outro ")
        except dns.resolver.NoAnswer:
            print(bcolor.color.FAIL + "Arrumar erro argumento vazio")
        except dns.exception.FormError:
            print(bcolor.color.FAIL + "ERROR: No answer or RRset not for qname")
            pass
        except ConnectionRefusedError:
            print(bcolor.color.FAIL + "(NXDOMAIN)NS  não permitido tente outro ")


        else:
            print(bcolor.color.WARNING + "[!] Transferencia de Zona Realizada !")
            registroDNS = trzf.nodes.keys()
            sorted(registroDNS)
            for i in registroDNS:
                print(trzf[i].to_text(i))

except:
    pass

print(bcolor.color.ENDC+"\t[+]EMAILs[+]")
agent ={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
#head_random = choice(agent)


req = requests.get("http://{}/index.html".format(sys.argv[1]), headers=agent).text

bs = bs4.BeautifulSoup(req, features='lxml')
var = bs.find_all(['p'])[-1]
mail = set(re.findall(r'[\w\.-]+@[\w\.-]+', var.text))
for element in mail:
        print("[!]", element)

bar()
print(bcolor.color.BOLD + "\n\t\t[+] WHOIS = Consulting ...\n")
time.sleep(5)
try:
    host = sys.argv[1]  # input("Informe o dominio =>")
    if host != float:
        ip = socket.gethostbyname(host)  # Convert url to ip
        print(ip)

        '''dnss = requests.get("https://who.is/dns/" + sys.argv[1]).text
        bs1 = bs4.BeautifulSoup(dnss, features='lxml')
        print(bs1.find_all('table'))'''

        # resp = requests.get("http://wq.apnic.net/apnic-bin/whois.pl?searchtext=" + data + "&form_type=advanced")
        resp = requests.get("https://who.is/whois-ip/ip-address/" + ip).text
        bs = bs4.BeautifulSoup(resp, features="lxml")
        soup = bs.find_all(['pre'])

        print(soup)


except socket.gaierror:
    pass
bar()
print("\t\t\n[+] BANNER GRAB ...\n")
sys.argv[1]  # input("\nInforme o host => ")  # o  importante é rodarh
https.__init__()
firewall.__init__()
bar()
banner.__init__()
bar()

sn = input("Digite o nome do arquivo.txt para vizualizar = ")
if sn != 0:
    try:
        os.system("CD \\Users\\DESKTOP\\PycharmProjects\\REDES\\")
        os.system("explorer {}".format(sn))
    except KeyboardInterrupt:
        pass  # indece deve da errado
    else:
        print(bcolor.color.FAIL + "[+] Programa encerado!")
    sys.exit()
    # python.exe karinr.py testphp.vulnweb.com
    # ta executando outro interpretador

    '''https://www.shodan.io/search?query='''
# despejar saida em um arquivo
