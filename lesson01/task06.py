"""
6.  Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование»,
    «сокет», «декоратор». Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате
    Unicode и вывести его содержимое.
"""

import chardet

WORDS = ['сетевое программирование', 'сокет', 'декоратор']

with open("test_file.txt", 'w+') as file_handler:
    for value in WORDS:
        file_handler.write(value + '\n')

with open("test_file.txt", encoding='utf-8') as file_handler:
    for line in file_handler:
        print(line)

# Результат вывода
# кодировка файла по умолчанию utf-8
# сетевое программирование
#
# сокет
#
# декоратор
