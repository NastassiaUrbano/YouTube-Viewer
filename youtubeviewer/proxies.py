"""
MIT License

Copyright (c) 2021-2023 MShawon

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys
from random import shuffle

import requests

from .colors import *


def gather_proxy():
    proxies = []
    print(bcolors.OKGREEN + 'Scraping proxies ...' + bcolors.ENDC)

    link_list = ['https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt',
                 'https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt',
                 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt',
                 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt',
                 'https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/proxy.txt',
                 'https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt'
                154.213.202.200:3128
104.207.55.133:3128
156.233.85.100:3128
156.228.101.106:3128
104.207.54.176:3128
104.167.25.26:3128
154.94.12.52:3128
104.207.42.109:3128
104.207.43.158:3128
104.207.63.35:3128
156.228.124.32:3128
156.228.180.77:3128
154.213.196.21:3128
154.213.194.33:3128
156.228.111.60:3128
104.207.50.145:3128
156.240.99.80:3128
154.213.204.58:3128
104.207.58.22:3128
156.233.84.37:3128
45.201.10.199:3128
156.228.83.164:3128
154.213.196.28:3128
156.253.172.142:3128
156.249.138.61:3128
156.253.168.242:3128
156.228.94.38:3128
156.228.76.140:3128
104.207.56.224:3128
154.94.14.114:3128
156.228.92.64:3128
156.253.174.214:3128
104.207.40.194:3128
156.249.138.255:3128
156.228.189.159:3128
156.228.96.84:3128
156.233.92.107:3128
156.228.97.73:3128
156.228.100.163:3128
104.207.60.192:3128
156.228.100.71:3128
154.213.203.85:3128
156.228.92.146:3128
156.228.115.180:3128
104.167.28.148:3128
104.167.29.243:3128
104.207.45.248:3128
156.228.101.77:3128
156.253.165.93:3128
156.228.111.91:3128
156.233.87.228:3128
156.228.181.41:3128
156.233.92.34:3128
104.207.43.21:3128
104.207.57.94:3128
156.228.99.123:3128
156.228.106.136:3128
156.228.0.45:3128
104.207.33.114:3128
156.233.75.208:3128
154.213.199.51:3128
156.228.80.93:3128
104.207.47.107:3128
156.233.89.14:3128
156.253.178.103:3128
104.207.56.62:3128
104.207.38.199:3128
156.228.119.147:3128
156.228.179.141:3128
156.233.94.65:3128
104.207.38.89:3128
104.207.62.109:3128
156.228.82.234:3128
156.253.176.119:3128
156.228.82.91:3128
156.228.108.253:3128
156.228.179.157:3128
154.213.194.244:3128
154.213.197.25:3128
156.228.84.9:3128
154.94.15.155:3128
104.207.37.31:3128
156.228.81.46:3128
156.233.85.6:3128
104.167.31.192:3128
156.228.182.201:3128
156.228.182.142:3128
156.228.180.78:3128
156.253.168.90:3128
156.253.173.140:3128
156.233.90.163:3128
156.249.138.176:3128
45.202.77.252:3128
154.213.198.78:3128
156.228.109.187:3128
156.228.124.67:3128
156.228.112.173:3128
156.228.184.196:3128
104.207.36.173:3128
104.207.61.44:3128
]

    for link in link_list:
        response = requests.get(link)
        output = response.content.decode()

        if '\r\n' in output:
            proxy = output.split('\r\n')
        else:
            proxy = output.split('\n')

        for lines in proxy:
            for line in lines.split('\n'):
                proxies.append(line)

        print(bcolors.BOLD + f'{len(proxy)}' + bcolors.OKBLUE +
              ' proxies gathered from ' + bcolors.OKCYAN + f'{link}' + bcolors.ENDC)

    proxies = list(set(filter(None, proxies)))
    shuffle(proxies)

    return proxies


def load_proxy(filename):
    proxies = []

    if not os.path.isfile(filename) and filename[-4:] != '.txt':
        filename = f'{filename}.txt'

    try:
        with open(filename, encoding="utf-8") as fh:
            loaded = [x.strip() for x in fh if x.strip() != '']
    except Exception as e:
        print(bcolors.FAIL + str(e) + bcolors.ENDC)
        input('')
        sys.exit()

    for lines in loaded:
        if lines.count(':') == 3:
            split = lines.split(':')
            lines = f'{split[2]}:{split[-1]}@{split[0]}:{split[1]}'
        proxies.append(lines)

    proxies = list(filter(None, proxies))
    shuffle(proxies)

    return proxies


def scrape_api(link):
    proxies = []

    try:
        response = requests.get(link)
        output = response.content.decode()
    except Exception as e:
        print(bcolors.FAIL + str(e) + bcolors.ENDC)
        input('')
        sys.exit()

    if '\r\n' in output:
        proxy = output.split('\r\n')
    else:
        proxy = output.split('\n')

    for lines in proxy:
        if lines.count(':') == 3:
            split = lines.split(':')
            lines = f'{split[2]}:{split[-1]}@{split[0]}:{split[1]}'
        proxies.append(lines)

    proxies = list(filter(None, proxies))
    shuffle(proxies)

    return proxies


def check_proxy(category, agent, proxy, proxy_type):
    if category == 'f':
        headers = {
            'User-Agent': f'{agent}',
        }

        proxy_dict = {
            "http": f"{proxy_type}://{proxy}",
            "https": f"{proxy_type}://{proxy}",
        }
        response = requests.get(
            'https://www.youtube.com/', headers=headers, proxies=proxy_dict, timeout=30)
        status = response.status_code

    else:
        status = 200

    return status
