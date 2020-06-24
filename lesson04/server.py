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
from socket import socket, AF_INET, SOCK_STREAM
from datetime import datetime

PARSER = argparse.ArgumentParser()

PARSER.add_argument('--a', help='IP-адрес для прослушивания', default='')
PARSER.add_argument('--p', help='TCP-порт для прослушивания', default=7777)

ARGS = PARSER.parse_args()

IP = ARGS.a
PORT = int(ARGS.p)

SOCS = socket(AF_INET, SOCK_STREAM)
SOCS.bind((IP, PORT))
SOCS.listen(True)

while True:
    CONN, ADDR = SOCS.accept()
    DATA = CONN.recv(1024)

    # примитивный лог подключений:)
    print('Подключился клиент: ', ADDR)

    DATA_ANSW = {'time': datetime.now().timestamp()}

    DATA_MSG = json.loads(DATA)
    if DATA_MSG['action'] == 'message':
        DATA_ANSW['action'] = 'message'
        DATA_ANSW['message'] = 'Привет клиент. Все хорошо:)'
        DATA_ANSW['response'] = 200
    elif DATA_MSG['action'] == 'status':
        DATA_ANSW['action'] = 'status'
        DATA_ANSW['message'] = 'OK'
        DATA_ANSW['response'] = 200
    else:
        DATA_ANSW['action'] = 'error'
        DATA_ANSW['response'] = 500

    CONN.send(json.dumps(DATA_ANSW).encode('utf-8'))
    CONN.close()

# Пример запуска сервера: server.py --a=127.0.0.1 --p=9001
# ------------------
# Подключился клиент:  ('127.0.0.1', 47034)
# Подключился клиент:  ('127.0.0.1', 47036)
# Подключился клиент:  ('127.0.0.1', 47038)
