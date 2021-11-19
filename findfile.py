import re
import sys

import requests

from bs4 import BeautifulSoup

head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/77.0.3865.90 '
                      'Safari/537.36'}


def proxy_test():
    """ Faz requisiçao ao site passando header e timeout procura a tag e traz o texto limpo"""

    req = requests.get("https://www.whatismyip.com", headers=head, timeout=10)
    bs = BeautifulSoup(req.text, 'lxml')
    ip = bs.find(id="ipv4").get_text()
    print(f"\tSeu IP :{ip}\n")


proxy_test()


def busca_resultados(metodo, busca, arquivo):
    """ Busca usando operadores do google arquivos indexados
        abre e retorna um conteudo aleatorio
    OBS: O Gloogle bloqueia essas requisiçoes uso de proxy"""
    global abre
    try:
        ban = ['https://policies.google.com/terms?hl=pt-BR&fg=1', 'https://policies.google.com/terms?hl=pt-BR&fg=1',
               'https://maps.google.com/', 'https://translate.google.com/', 'https://www.youtube.com,',
               'https://www.airbnb.com.br', 'https://webcache.googleusercontent.com',
               'https://support.google.com/websearch/answer/181196?hl=pt-BR']

        parametro = {'q': metodo + busca + arquivo, 'start': 0, 'num': 10}
        req = requests.get(url='https://www.google.com/search', params=parametro, headers=head, timeout=10)
        bs = BeautifulSoup(req.content, 'lxml')
        print(f"BUSCANDO NO {req.url}\n")

        for link in set(bs.findAll('a', href=re.compile('^(http)|(https)|(ftp)((?!' + req.url + ').)*$'))):

            if link["href"].startswith('http'):
                print('\033[33m''[+][ENCONTRADO][+]''\033[36m' + link.attrs['href'] + '\n')

            abre = requests.get(url=link.attrs['href'], headers=head, timeout=30)
            bs2 = BeautifulSoup(abre.text, 'lxml')

            print(bs2.get_text())

    except requests.exceptions.InvalidSchema:
        print(F"[!][ERRO][!] URL INVALIDA {abre.url}")
    except KeyboardInterrupt:
        print("\n[x][Encerrado[x]\n")
        sys.exit(3)


# requests.exceptions.ReadTimeout
# requests.exceptions.InvalidSchema:
busca_resultados(metodo='kom', busca='ombo', arquivo='temple')
