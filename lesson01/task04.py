"""
4.  Преобразовать слова «разработка», «администрирование», «protocol», «standard»
    из строкового представления в байтовое и выполнить обратное преобразование (используя методы encode и decode).
"""

WORDS = ['разработка', 'администрирование', 'protocol', 'standard']

for value in WORDS:
    enc_value = value.encode('utf-8')
    dec_value = enc_value.decode('utf-8')
    print(value, ' - ', enc_value, ' - ', dec_value)

# Результат вывода
# разработка  -  b'\xd1\x80\xd0\xb0\xd0\xb7\xd1\x80\xd0\xb0\xd0\xb1\xd0\xbe\xd1\x82\xd0\xba\xd0\xb0'
# -  разработка
#
# администрирование  -  b'\xd0\xb0\xd0\xb4\xd0\xbc\xd0\xb8\xd0\xbd\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0
# \xb8\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5'  -  администрирование
#
# protocol  -  b'protocol'  - protocol
#
# standard  -  b'standard'  -  standard
