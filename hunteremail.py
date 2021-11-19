import json
import sys
from urllib.request import urlopen


def email_hunter():
    """API Hunter.io """
    print("'\033[1m'\t[+] RECON ...\t\n")

    key = '6a5b4fa748e6bbe572c5470f0f44d92c78ff59aa'

    req = urlopen(
        f"https://api.hunter.io/v2/domain-search?domain={sys.argv[1]}&api_key={key}")
    "https://api.hunter.io/v2/domain-search?domain={}&api_key=6a5b4fa748e6bbe572c5470f0f44d92c78ff59aa"

    rjson = json.load(req)
    # print(rjson['data']['emails'][0])

    for item in rjson['data']['emails']:
        for chave, valor in item.items():
            print(chave.capitalize(), "\t|\t", valor)


email_hunter()
