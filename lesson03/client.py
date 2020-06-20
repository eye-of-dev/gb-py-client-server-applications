"""
    Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
    клиент отправляет запрос серверу;
    Функции клиента:
        сформировать presence-сообщение;
        отправить сообщение серверу;
        получить ответ сервера;
        разобрать сообщение сервера;
        параметры командной строки скрипта client.py <addr> [<port>]:
            addr — ip-адрес сервера;
            port — tcp-порт на сервере, по умолчанию 7777.
"""

import argparse
import json
from socket import *
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument('--a', help='IP-адрес для подключения', default='localhost')
parser.add_argument('--p', help='TCP-порт для подключения', default=7777)

args = parser.parse_args()

ip = args.a
port = int(args.p)

data_msg1 = {'action': 'status'}
data_msg2 = {'action': 'message', 'message': 'Привет сервер. Как дела?'}
data_msg3 = {'action': 'error'}

messages = [data_msg1, data_msg2, data_msg3]
for message in messages:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((ip, int(port)))

    message['time'] = datetime.now().timestamp()
    s.send(json.dumps(message).encode('utf-8'))
    data = s.recv(1000000)

    s.close()
    data_answ = json.loads(data)
    if data_answ['response'] == 200:
        print(data_answ['message'])
    else:
        print('что-то пошло не так:(')


# Пример запуска клиета: client.py --a=127.0.0.1 --p=9001
# --------------
# OK
# Привет клиент. Все хорошо:)
# что-то пошло не так:(
