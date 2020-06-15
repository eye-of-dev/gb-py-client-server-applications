"""
2.  Каждое из слов «class», «function», «method» записать в байтовом типе без
    преобразования в последовательность кодов (не используя методы encode и decode) и
    определить тип, содержимое и длину соответствующих переменных.
"""

WORDS_B = [b'class', b'function', b'method']

for value in WORDS_B:
    print(value, ' - ', type(value), ' - длина:', len(value))

# Результат вывода
# b'class'  -  <class 'bytes'>  - длина: 14
# b'function'  -  <class 'bytes'>  - длина: 8
# b'method'  -  <class 'bytes'>  - длина: 6
