"""
    Реализовать простое клиент-серверное взаимодействие по протоколу JIM (JSON instant messaging):
    сервер отвечает соответствующим кодом результата.
    Функции сервера:
        принимает сообщение клиента;
        формирует ответ клиенту;
        отправляет ответ клиенту;
        имеет параметры командной строки:
            -p <port> — TCP-порт для работы (по умолчанию использует 7777);
            -a <addr> — IP-адрес для прослушивания (по умолчанию слушает все доступные адреса).
"""

import argparse
import json
from socket import *
from datetime import datetime

parser = argparse.ArgumentParser()

parser.add_argument('--a', help='IP-адрес для прослушивания', default='')
parser.add_argument('--p', help='TCP-порт для прослушивания', default=7777)

args = parser.parse_args()

ip = args.a
port = int(args.p)

sock = socket(AF_INET, SOCK_STREAM)
sock.bind((ip, port))
sock.listen(True)

while True:
    conn, addr = sock.accept()
    data = conn.recv(1000000)

    # примитивный лог подключений:)
    print('Подключился клиент: ', addr)

    data_answ = {'time': datetime.now().timestamp()}

    data_msg = json.loads(data)
    if data_msg['action'] == 'message':
        data_answ['action'] = 'message'
        data_answ['message'] = 'Привет клиент. Все хорошо:)'
        data_answ['response'] = 200
    elif data_msg['action'] == 'status':
        data_answ['action'] = 'status'
        data_answ['message'] = 'OK'
        data_answ['response'] = 200
    else:
        data_answ['action'] = 'error'
        data_answ['response'] = 500

    conn.send(json.dumps(data_answ).encode('utf-8'))
    conn.close()

# Пример запуска сервера: server.py --a=127.0.0.1 --p=9001
# ------------------
# Подключился клиент:  ('127.0.0.1', 47034)
# Подключился клиент:  ('127.0.0.1', 47036)
# Подключился клиент:  ('127.0.0.1', 47038)
