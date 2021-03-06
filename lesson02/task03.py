"""
3.  Задание на закрепление знаний по модулю yaml. Написать скрипт,
    автоматизирующий сохранение данных в файле YAML-формата.

    Для этого:
    *   Подготовить данные для записи в виде словаря, в котором первому
        ключу соответствует список, второму — целое число, третьему —
        вложенный словарь, где значение каждого ключа — это целое число
        с юникод-символом, отсутствующим в кодировке ASCII (например, €);
    *   Реализовать сохранение данных в файл формата YAML — например,
        в файл file.yaml. При этом обеспечить стилизацию файла с помощью
        параметра default_flow_style, а также установить возможность
        работы с юникодом: allow_unicode = True;
    *   Реализовать считывание данных из созданного файла и проверить,
        совпадают ли они с исходными.
"""
import yaml

TO_YAML = {
    "key_one": ['a', 1, '元'],
    "key_two": 100,
    "key_three": {
        "price_one": '10€',
        "price_two": '10000₽'
    },
}

with open('data/data_write.yaml', 'w') as file_handler:
    yaml.dump(TO_YAML, file_handler, default_flow_style=False, allow_unicode=True)

with open('data/data_write.yaml') as file_handler:
    print(file_handler.read())

# Вывод содержимога файла
# key_one:
# - a
# - 1
# - 元
# key_three:
#   price_one: 10€
#   price_two: 10000₽
# key_two: 100
