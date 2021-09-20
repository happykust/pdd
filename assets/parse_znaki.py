import requests, json, os
from bs4 import BeautifulSoup

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

result = []

print("[***] Script by @happykust | PDD signs parser [***]")
print("[+] Starting...")

url_main = 'https://xn----8sbkahkuskl1n.com/pdd/znaki-pdd/znaki/russia.html'

html = requests.get(url_main, headers=headers).text

page = BeautifulSoup(html, 'lxml')

links = [x.get("href").replace('..', 'https://xn----8sbkahkuskl1n.com/pdd/znaki-pdd') for x in page.select('.box > p > a')[:9]]

for i, link in enumerate(links):
    link_html = requests.get(link, headers=headers).text
    link_page = BeautifulSoup(link_html, 'lxml')

    page_header = link_page.select_one('.box > h1').text.split(' ', 1)[1]

    print('[+] Parsing:', page_header)

    if not os.path.exists(f'./assets/imgs/signs/{i}'):
        os.mkdir(f'./assets/imgs/signs/{i}')

    znaks = []

    for j, znak_html in enumerate(link_page.select('.box > div')):
        if not znak_html.select('img'):
            continue
        img_url = 'https://' + '/'.join(link.replace('https://', '').split('/')[:4]) + '/' + znak_html.select_one('img').get('src')
        znak_description = znak_html.text.replace('\n', ' ')
        img = requests.get(img_url, headers=headers)
        img_res = znak_html.select_one('img').get('src').split('.')[-1]
        with open(f'./assets/imgs/signs/{i}/{j}.{img_res}', 'wb') as f:
           f.write(img.content)
        img_assets_url = f'./assets/imgs/signs/{i}/{j}.{img_res}'
        znaks.append({'image_url': img_assets_url, 'desc': znak_description})
    
    result.append({'title': page_header, 'signs': znaks})

with open('signs.json', 'w', encoding='UTF-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print('[+] Parsing ended successfully!')
input('Press any key to exit...')
