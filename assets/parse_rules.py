import json, requests
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

result = []

url_list = 'https://xn----8sbkahkuskl1n.com/pdd/pdd-rus/pdd/russia.html'

url_test = 'https://xn----8sbkahkuskl1n.com/pdd/pdd-rus/4-prava/peshehodov.html'

r = requests.get(url_test, headers=headers).text

b = BeautifulSoup(r, 'lxml')

box = b.select_one('.box').children


el = []
for bx in box:
    if bx.name == None:
        continue
    if bx.name == 'h1':
        print('Заголовок -', bx.text)
        continue
    if bx.name != 'hr':
        el.append(bx.text)
    else:
        print(*el)
        print()
        el = []