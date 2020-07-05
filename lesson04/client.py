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
import logging
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime

from lesson04.decorators import log
from lesson04.log import client_log_config

LOG = logging.getLogger('app.client')

PARSER = argparse.ArgumentParser()

PARSER.add_argument('--a', help='IP-адрес для подключения', default='localhost')
PARSER.add_argument('--p', help='TCP-порт для подключения', default=7777)

ARGS = PARSER.parse_args()

IP = ARGS.a
PORT = int(ARGS.p)


@log
def create_message(action, message=None):
    """
    Create message for server
    :param action: Action
    :param message: Message
    :return: Set
    """
    return {
        'action': action,
        'message': message,
        'time': datetime.now().timestamp()
    }


DATA_MSG1 = create_message('status')
DATA_MSG2 = create_message('message', 'Привет сервер. Как дела?')
DATA_MSG3 = create_message('error')

MESSAGES = [DATA_MSG1, DATA_MSG2, DATA_MSG3]
for message in MESSAGES:
    s = socket(AF_INET, SOCK_STREAM)
    s.connect((IP, int(PORT)))

    try:
        s.send(json.dumps(message).encode('utf-8'))
    except Exception as e:
        LOG.error(f'An error occurred : {str(e)}')

    data = s.recv(1024)

    s.close()
    data_answ = json.loads(data)
    if data_answ['response'] == 200:
        print(data_answ['message'])
    else:
        LOG.error('что-то пошло не так:(')

# Пример запуска клиета: client.py --a=127.0.0.1 --p=9001
# --------------
# 2020-07-05 14:49:01,885 - ERROR app.client что-то пошло не так:(
# 2020-07-05 15:15:27,507 - INFO app.client filename: client.py func name: create_message and func args: ('status',), {}
# 2020-07-05 15:15:27,507 - INFO app.client filename: client.py func name: create_message and func args:
# ('message', 'Привет сервер. Как дела?'), {}
# 2020-07-05 15:15:27,507 - INFO app.client filename: client.py func name: create_message and func args: ('error',), {}

# Примечание:
# Сообщение INFO - логирование из декоратора. Логирует файл откуда была вызван декоратор, имя функции, параметры функции
