"""
3.  Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.
"""

WORDS_B = [b'attribute', b'класс', b'функция', b'type']

for value in WORDS_B:
    print(value, ' - ', type(value))

# Результат вывода
# WORDS_B = [b'attribute', b'класс', b'функция', b'type']
# SyntaxError: bytes can only contain ASCII literal characters.
# Символы кирилицы не входят в кодировку ASCII,
# соответственно слова "класс", "функция" невозможно записать в байтовом типе

