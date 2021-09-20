import json, requests, re
from bs4 import BeautifulSoup
from requests.api import head

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

result = []

print("[***] Script by @happykust | PDD signs parser [***]")
print("[+] Starting...")

url_list = 'https://xn----8sbkahkuskl1n.com/pdd/pdd-rus/pdd/russia.html'

r = requests.get(url_list, headers=headers).text

page = BeautifulSoup(r, 'lxml')

links = [x.get("href").replace('..', 'https://xn----8sbkahkuskl1n.com/pdd/pdd-rus') for x in page.select('.box > p > a')[:26]]

for i, link in enumerate(links):
    link_html = requests.get(link, headers=headers).text
    link_page = BeautifulSoup(link_html, 'lxml')

    box = link_page.select_one('.box').children

    header = ''

    rules = []
    el = []
    for bx in box:
        if bx.name == None:
            continue
        if bx.name == 'h1':
            header = bx.text
            continue
        if bx.name != 'hr':
            el.append(bx.text)
        else:
            st = ''
            for l in el:
                st += " ".join(f' {l}'.replace('"', "").replace("\n", " ").split())
            rules.append(st)
            el = []

    print('[+] Parsed:', header)

    result.append({'title': header, 'rules': rules})

with open('rules.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print('[+] Parsing ended successfully!')
input('Press any key to exit...')
