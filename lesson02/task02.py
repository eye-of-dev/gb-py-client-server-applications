"""
2.  Задание на закрепление знаний по модулю json.

    Есть файл orders в формате JSON с информацией о заказах.
    Написать скрипт, автоматизирующий его заполнение данными.
    Для этого:
    *   Создать функцию write_order_to_json(), в которую передается
        5 параметров — товар (item), количество (quantity), цена (price),
        покупатель (buyer), дата (date). Функция должна предусматривать
        запись данных в виде словаря в файл orders.json. При записи данных
        указать величину отступа в 4 пробельных символа;
    *   Проверить работу программы через вызов функции write_order_to_json()
        с передачей в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    """
    Записать данные в json файл
    :param item: Товар
    :param quantity: Количество
    :param price: Цена
    :param buyer: Покупатель
    :param date: Дата
    :return: None
    """
    to_json = {
        "item": item,
        "quantity": quantity,
        "price": price,
        "buyer": buyer,
        "date": date
    }

    with open('data/orders.json') as f_h:
        f_c = f_h.read()
        if f_c:
            from_json = json.loads(f_c)
        else:
            from_json = {'orders': []}

    if "orders" in from_json:
        from_json['orders'].append(to_json)
    else:
        orders = [to_json]
        from_json['orders'] = orders

    with open('data/orders.json', 'w') as f_h:
        json.dump(from_json, f_h, indent=4)


write_order_to_json('Кросовки Nike', 1, 3200, 'Антон Л.', 1592329631)

with open('data/orders.json') as file_handler:
    file_content = file_handler.read()
    json_data = json.loads(file_content)

print(json_data)

# Вывод содержимога файла
# {'orders': [{
#   'item': 'Кросовки Nike',
#   'quantity': 1,
#   'price': 3200,
#   'buyer': 'Антон Л.',
#   'date': 1592329631}]}
