import json
import re
from time import sleep
from urllib.request import urlopen

import requests
from bs4 import BeautifulSoup

"""INDEX DO GOOGLE """

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.90 '
                      'Safari/537.36',

        }

def procura_s(metodo, domain, metodo2):
    global proxie, proxybreak
    global proxies
    global head
    global f
    proxies = {
        "http": "http://66.119.169.237:80",
        "https": "http://103.78.254.78:80"
    }

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/77.0.3865.90 '
                          'Safari/537.36',

            }

    parametro = {'q': metodo + domain + metodo2, 'start': 0, 'num': 10}
    url = 'https://www.google.com/search'
    # http://www.fundflowmanagers.com/mns.txt
    try:
        with open('Free_Proxy_List.txt', 'r') as f:
            req = requests.get('https://www.google.com/search', params=parametro, headers=head, timeout=10,
                               proxies={"http": proxie})

            bs = BeautifulSoup(req.content, 'lxml')
            print('\n\t', req.url, '\t\n')

        # proxybreak = BeautifulSoup(req.text, 'lxml')

        # print(proxybreak.get_text())

        for link in set(bs.findAll('a', href=re.compile('^(http)|(https)|(ftp)((?!' + url + ').)*$'))):
            sleep(0.1)
            if link["href"].startswith('http'):
                print('\033[33m''[+][FOUND][+]''\033[36m' + link.attrs['href'] + '\n')
                # return link.attrs['href']'''

    except requests.exceptions.ProxyError:
        print('\033[41m'"[!]Nao foi possivel conectar ao proxy[!]"'\033[0;0m\n''\033[1m')

        resp = "Our systems have detected unusual traffic from your computer network." \
               " This page checks to see if it's really you sending the requests, and not a robot. "
        if resp in proxybreak.get_text():
            pass


# procura_s(metodo='python', domain='"python"', metodo2='python')


def proxy_test():
    # prox = input("[?] Insira o seu proxie : ")

    p = {
        "http": f"http://{'prox'}:80",

    }
    try:

        # os.popen('anonsurf start')

        req = requests.get("https://www.whatismyip.com", headers=head, timeout=10)
        sleep(3)
        bs = BeautifulSoup(req.text, 'lxml')
        ip = bs.find('span',
                     class_="cf-footer-separator sm:hidden").findNext().get_text()  # 'span', {'class':"cf-footer
        # -item sm:block sm:mb-1"}).get_text()
        print(ip)
    except AttributeError:
        pass
    except requests.exceptions.ReadTimeout:
        print('\033[41m'"[!] Tempo de conexao excedido "'\033[0;0m\n''\033[1m')
    except requests.exceptions.ProxyError:
        print('\033[41m'"[!] Nao foi possivel conectar ao proxy "'\033[0;0m\n''\033[1m')


proxy_test()


def request(var):
    try:  # Our systems have detected unusual traffic from your computer network. This page checks to see if it's
        # really you sending the requests, and not a robot.
        req = requests.get(url=var, headers=head)
        print(req.url)
        bs = BeautifulSoup(req.content, 'lxml')
        bs.findAll('pre')
        print(bs.get_text())

    except requests.exceptions.MissingSchema:
        print('\033[41m'f"ERROR[!]: Url Invalida"'\033[0;0m\n''\033[1m')
    except requests.exceptions.ProxyError:
        print('\033[41m'f"ERROR[!]: Nao foi possivel conectar ao proxy"'\033[0;0m\n''\033[1m')


# request(var='http://www.fundflowmanagers.com/mns.txt')


def email_l(domain):
    print("'\033[1m'\t[+] RECON ...\t\n")
    sleep(2)
    key = '6a5b4fa748e6bbe572c5470f0f44d92c78ff59aa'

    req = urlopen(
        f"https://api.hunter.io/v2/domain-search?domain={domain}&api_key={key}")
    "https://api.hunter.io/v2/domain-search?domain={}&api_key=6a5b4fa748e6bbe572c5470f0f44d92c78ff59aa"

    rjson = json.load(req)
    # print(rjson['data']['emails'][0])

    for item in rjson['data']['emails']:
        for chave, valor in item.items():
            print(chave.capitalize(), "\t|\t", valor)


