import argparse
import socket

import dns
import dns.resolver
import dns.zone


def dns_enum(domain):
    """___"""
    try:
        print('\033[36m''\t[+] CONSULT DNS ...\t\n''\033[0;0m''\033[1m')

        lista = ['A', 'AAAA', 'CNAME', 'MX', 'NS', 'TXT', 'CAA', ' RP', 'SOA', 'SRV', 'PTR', 'SPF', 'DNAME']

        for tipo in lista:

            req = dns.resolver.query(domain, tipo, raise_on_no_answer=False)
            if req.rrset is not None:
                print(req.rrset)

            """re2 =  dns.resolver.query(domain, lista[2])
                if re2.rrset is not None:
                    for i in re2:
                        print(f"{domain} {i}")
            #dns.resolver.NoAnswer: The DNS response does not contain an answer to the question: google.com. IN CNAME"""

    except dns.rdatatype.UnknownRdatatype:
        print('\033[41m''[!] ERROR : Dns resource record type is unknown.[!]''\033[0;0m\n''\033[1m')
    except dns.resolver.NXDOMAIN:
        print('\033[41m'f"[!] ERROR : The DNS query name does not exist : {domain}'\033[0;0m\n''\033[1m'")


def dns_xfr(domain):
    """___"""
    registrons = dns.resolver.query(domain, "NS")
    lista = []

    for registro in registrons:
        lista.append(str(registro))
    for registro in lista:
        try:

            transfzona = dns.zone.from_xfr(dns.query.xfr(registro, domain))

        except dns.exception.FormError:
            print('\033[41m'"[!]ERRO[!] No answer or RRset not for qname:"'\033[0;0m\n''\033[1m')
            pass
        except dns.resolver.NoAnswer:
            print('\033[41m'"[!]ERRO[!]The DNS response does not contain an answer to the question: {} IN "
                  "NS"'\033[0;0m\n''\033[1m'.format(domain))
            pass
        except dns.exception.SyntaxError:
            pass
        except ValueError:
            pass
        except dns.resolver.NXDOMAIN:
            print("None of DNS query names exist: {}".format(domain))
            pass
        except EOFError:
            pass
        else:
            print('\033[43m'"[+]Tranferência de Zona Realizada[+]"'\033[0;0m''\033[1m')
            registroDNS = transfzona.nodes.keys()

            for n in registroDNS:
                print(transfzona[n].to_text(n), "\n")


def dns_bruto(domain):
    """ ___"""
    print('\033[36m'"\n\t[+] FORÇA"'\033[0;0m''\033[1m''\n')
    with open("hlist.txt") as arquivo:
        wordlist = arquivo.readlines()
    for nome in wordlist:
        ddns = nome + domain

        print(ddns + '|' + socket.gethostbyname(ddns))


def grab(host):
    """ """

    for porta in (21, 22, 23, 25, 53, 80, 111, 10000, 445):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            sock.connect((host, porta))

            saida = sock.recv(1024)
            # print('[i] bytes', len(saida))

            if saida == 0:
                print(f"[+] Test | {saida} | {host} | {porta} | {'socket.getservbyport().upper()'}")
                # print('[!]Nao recebido', len(saida), ' bytes')
            else:
                print(f"[+] Test | {saida} | {host} | {porta} | {'socket.getservbyport().upper()'}")

        except ConnectionAbortedError:
            print(f"[!] Error [!] {host} | Porta | {porta} | Drop?")

        except ConnectionRefusedError:

            print(f"[!] Error [!] {host} | Porta | {porta} | Fechada?")
            pass
        except ConnectionResetError:
            print(f"[!] Error [!] {host} | Porta | {porta} | Filtrada?")
        except ConnectionError:
            print(f"[!] Error [!] {host} | Porta | {porta} | [?]")


# OSError: [Errno 113] No route to hos
def main():
    """AAAAAAAAAAAAAA"""

    banner = '\033[1m' + """NAO VOU DESISTIR DA MINHA FAMILIA"""
    # print(banner)

    vermelho = '\033[31m'
    verde = '\033[32m'
    azul = '\033[34m'

    ciano = '\033[36m'
    magenta = '\033[35m'
    amarelo = '\033[33m'
    preto = '\033[30m'

    branco = '\033[37m'

    original = '\033[0;0m'
    negrito = '\033[1m'
    reverso = '\033[2m'

    preto = '\033[40m'

    vermelho = '\033[41m'

    verde = '\033[42m'

    amarelo = '\033[43m'

    azul = '\033[44m'

    magenta = '\033[45m'

    ciano = '\033[46m'


if __name__ == '__main__':
    # parse = argparse.ArgumentParser(description="[+] Test informaçao")
    # parse.add_argument('host', nargs='?', default='127.0.0.1', help='[i] Insira o host')
    # parse.add_argument('-p', type=int, metavar='porta', help='[i] Insira a porta')
    # parse.print_help()

    print(f"[i]", socket.gethostbyname(socket.getfqdn()))
    grab(host='')
    # dns_enum(parse.parse_args().domain)
    # dns_bruto(parse.parse_args().domain)
    # dns_xfr(parse.parse_args().domain)
