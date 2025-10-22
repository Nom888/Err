import random
import re

from PyRoxy import ProxyChecker, ProxyUtiles
from colorama import Fore, init
import requests

prx = [
    "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt"
]
session = requests.Session()
init()

send = 0
total = 0
naxui = random.randint(1000, 9999)
for url in prx:
    send += 1
    req = session.get(url).text
    req = re.sub(r"^\s+|\s+$", "", re.sub(r"^\s*$\n?", "", req, flags=re.MULTILINE), flags=re.MULTILINE).splitlines()

    if "socks5" in url:
        req = ["socks5://" + prox.lstrip("socks5://") for prox in req]

    elif "socks4" in url:
        req = ["socks4://" + prox.lstrip("socks4://") for prox in req]

    elif "https" in url:
        req = ["https://" + prox.lstrip("https://") for prox in req]

    elif "http" in url:
        req = ["http://" + prox.lstrip("http://") for prox in req]

    total += len(req)
    print(Fore.YELLOW + f"[{send}]" + Fore.GREEN, url, f"| {len(req)}" + Fore.RESET)

    with open(f"bazadian{naxui}.txt", "a", encoding="utf-8") as f:
        f.write("\n".join([re.sub(r"^(([^:]+:){2}[^:]+):.*$", r"\1", prox) for prox in req]) + "\n")

print(Fore.BLUE + f"total {total}\n" + Fore.RESET)

proxies = ProxyUtiles.readFromFile(f"bazadian{naxui}.txt")

result = ProxyChecker.checkAll(proxies, url="http://gw.sandboxol.com", threads=1000)

blyat = "epta"
with open(f"{blyat}.txt", "a", encoding="utf-8") as f:
    for proxy in result:
        f.write(f"{proxy.type.name.lower()}://{proxy.host}:{proxy.port}\n")

with open(f"{blyat}.txt", encoding="utf-8") as f:
    print(Fore.RED + f"file {blyat}.txt | success {len(f.readlines()) - 1}" + Fore.RESET)
