"""
1.  Задание на закрепление знаний по модулю CSV.

    Написать скрипт, осуществляющий выборку определенных данных из файлов info_1.txt,
    info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
    Для этого:
    *   Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
        с данными, их открытие и считывание данных. В этой функции из считанных
        данных необходимо с помощью регулярных выражений извлечь значения параметров
        «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
        каждого параметра поместить в соответствующий список. Должно получиться четыре
        списка — например, os_prod_list, os_name_list, os_code_list, os_type_list.
        В этой же функции создать главный список для хранения данных отчета — например,
        main_data — и поместить в него названия столбцов отчета в виде списка:
        «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
        для этих столбцов также оформить в виде списка и поместить в файл main_data
        (также для каждого файла);
    *   Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
        В этой функции реализовать получение данных через вызов функции get_data(),
        а также сохранение подготовленных данных в соответствующий CSV-файл;
    *   Проверить работу программы через вызов функции write_to_csv().
"""
import csv
import re


def get_data(files):
    """
    Извлекает данные из переданных для обработки файлов
    :param files: Массив(список) файлов для обработки
    :return: Двумерный массив(список) с данными
    """

    main_data = [['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']]

    for file in files:
        os_prod, os_name, os_code, os_type = None, None, None, None

        # кодировку файла определил вручную
        # chardetect lesson02/data/info_1.txt
        # lesson02/data/info_1.txt: windows - 1251 with confidence 0.9237003416621283
        with open(file, encoding='windows-1251') as file_handler:
            file_data = file_handler.read()

            spam = re.search(r"(Изготовитель системы):(.+)", file_data)
            if spam:
                os_prod = spam.groups()[1].strip()

            spam = re.search(r"(Название ОС):(.+)", file_data)
            if spam:
                os_name = spam.groups()[1].strip()

            spam = re.search(r"(Код продукта):(.+)", file_data)
            if spam:
                os_code = spam.groups()[1].strip()

            spam = re.search(r"(Тип системы):(.+)", file_data)
            if spam:
                os_type = spam.groups()[1].strip()

        main_data.append([os_prod, os_name, os_code, os_type])

    return main_data


def write_to_csv(main_data):
    """
    Запись данных в csv-файл
    :param main_data: Двумерный массив(список) с данными
    :return: None
    """
    with open('data/data_write.csv', 'w') as file_handler:
        file_handler_writer = csv.writer(file_handler)
        for row in main_data:
            file_handler_writer.writerow(row)


FILES = ['data/info_1.txt', 'data/info_2.txt', 'data/info_3.txt']

DATA = get_data(FILES)
write_to_csv(DATA)
