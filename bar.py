import time

from tqdm import tqdm
from bcolor import bcolor
def __init__():
    for i in tqdm(range(100)):
        time.sleep(0.1)
    tqdm.write(bcolor.color.OKGREEN+"[!]CONCLUIDO[!]")