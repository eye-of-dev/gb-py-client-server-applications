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
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime

PARSER = argparse.ArgumentParser()

PARSER.add_argument('--a', help='IP-адрес для подключения', default='localhost')
PARSER.add_argument('--p', help='TCP-порт для подключения', default=7777)

ARGS = PARSER.parse_args()

IP = ARGS.a
PORT = int(ARGS.p)

DATA_MSG1 = {'action': 'status'}
DATA_MSG2 = {'action': 'message', 'message': 'Привет сервер. Как дела?'}
DATA_MSG3 = {'action': 'error'}

MESSAGES = [DATA_MSG1, DATA_MSG2, DATA_MSG3]
for message in MESSAGES:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((IP, int(PORT)))

    message['time'] = datetime.now().timestamp()
    s.send(json.dumps(message).encode('utf-8'))
    data = s.recv(1024)

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
