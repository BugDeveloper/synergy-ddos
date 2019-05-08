import os
import requests
from urllib.parse import quote
import random
from random import randint
from moving_out import move_out

file = open('names.txt', 'r')
names = file.read().split(', ')

link = 'https://synergy.ru/lander/alm/lander.php?r=land/' \
       'index&unit=synergy&land=synergy.ru&type=univer' \
       '&version=index&form=home-b&graccount=synergy&grcampaign=e_mail_chain_vpo'

form_count = 0
success_message = 'Спасибо, ваше сообщение получено!'

while True:
    name = random.choice(names)
    phone_number = f'%2B7(9{randint(11, 99)}){randint(101, 500)}-{randint(10, 99)}-{randint(10, 99)}'
    payload = {
        'name': quote(name),
        'phone': phone_number,
        'personalDataAgree': 'on',
        'url': 'https%3A%2F%2Fsynergy.ru%2F%3Futm_source%3Dthanks%26',
    }
    try:
        r = requests.post(link, data=payload)
        status, content = r.status_code, r.content.decode()

        if success_message in content:
            form_count += 1
        else:
            print('Something went wrong.. Logging.')
            with open("log.txt", "a") as log_file:
                log_file.write(content + '\n\n\n')

        if form_count % 50 == 0:
            print(f'{form_count} forms have been submitted.')

    except ConnectionError:
        print('We have been banned. Moving out..')
        r = requests.get('http://169.254.169.254/metadata/v1/id')
        move_out(r.content)
        break
