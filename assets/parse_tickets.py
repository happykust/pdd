import requests, json, os

result = []

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}

def get_full_url(num):
    """ Returns full url to json file. Starts with 0 """
    return f'https://xn----8sbkahkuskl1n.com/stat26012020/quest/ab/bilet/b{num}.json'

def parse_json(content, num):
    json_ticket = json.loads(content)
    questions = []

    for indq, question in enumerate(json_ticket):
        answers = []
        image = None
        for index, answer in enumerate(question['v']):
            if answer == None:
                continue
            answers.append({'answer': answer, 'is_correct': str(question['otvet']) == str(index+1)})
        try:
            question['realUrl']
            img = requests.get(f'https://xn----8sbkahkuskl1n.com/stat26012020/img/ab/{num}_{indq+1}.jpg', headers=headers)
            if not os.path.exists(f'./assets/imgs/tickets/{num}'):
                os.mkdir(f'./assets/imgs/tickets/{num}')
            with open(f'./assets/imgs/tickets/{num}/{indq+1}.jpg', 'wb') as f:
                f.write(img.content)
            image = f'/assets/imgs/tickets/{num}/{indq+1}.jpg'
        except:
            pass
        questions.append({'question': question['quest'], 'description': question['comments'], 'answers': answers, 'image': image})

    result.append({'ticket_number': num, 'questions': questions})

def get_ticket_json(num):
    """ Returns json of {num} ticket """
    url = get_full_url(num)
    return requests.get(url, headers=headers).text

def for_tickets():
    """ Gets all 20 tickets """
    for ticket_num in range(1, 21):
        print(f'[+] Getting {ticket_num} ticket...')
        text = get_ticket_json(ticket_num)
        parse_json(text, ticket_num)

if __name__ == "__main__":
    print("[***] Script by @happykust | PDD tickets parser [***]")
    print("[+] Starting...")
    for_tickets()
    with open('tickets.json', 'w', encoding='UTF-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print('[+] Parsing ended successfully!')
    input('Press any key to exit...')