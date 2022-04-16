# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные) файл логов web-сервера
# nginx_logs.txt (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs)
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]
#
# Примечание: код должен работать даже с файлами, размер которых превышает объем ОЗУ компьютера.
# Ответ на примечание: Оператор with открывает и закрывает файл, включая исключение внутреннего блока,
# он автоматически использует буферизованный ввод-вывод и управление памятью, поэтому не нужно беспокоиться о
# больших файлах.

import requests

def get_data():
    url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'

    with open("nginx_logs.txt", 'wb') as file:
        data = requests.get(url)
        file.write(data.content)

    try:
        with open("nginx_logs.txt", 'r') as file:
            temp = file.read()

    except FileNotFoundError:
        print("Файл не был создан")

    temp = temp.split('\n')

    result = []

    if temp[0]:
        temp = [i.split(' ') for i in temp][:len(temp) - 1]
        for i in temp:
            result.append((i[0], i[5][1:], i[6], '\n'))
        return result


print(get_data())


# 2. * (вместо 1) Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего
# задания. Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.

def analysis(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


try:
    with open("nginx_logs.txt", 'r') as file:
        temp = file.read()
        temp = temp.split('\n')

        result = []

        if temp[0]:
            temp = [i.split(' ') for i in temp][:len(temp) - 1]
            for i in temp:
                result.append(i[0])

        slovar = {}

        analysis(result, slovar)

        max_val = max(slovar.items(), key=lambda x: x[1])

        print(max_val)

except FileNotFoundError:
    print("Файл не был создан")


# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби. Известно, что при
# хранении данных используется принцип: одна строка — один пользователь, разделитель между значениями — запятая.

# Написать код, загружающий данные из обоих файлов и формирующий из них словарь: ключи — ФИО, значения — данные о хобби.
# Сохранить словарь в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей,
# чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1». При решении задачи
# считать, что объём данных в файлах во много раз меньше объема ОЗУ.

# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович

# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи
#
try:
    with open("users.csv", 'r', encoding='utf-8') as f_users:
        users = f_users.read()
        users = users.split('\n')
        users = [i for i in users][:-1]


except FileNotFoundError:
    print("Файл не был создан")

try:
    with open("hobby.csv", 'r', encoding='utf-8') as f_hobby:
        hobby = f_hobby.read()
        hobby = hobby.split('\n')
        hobby = [i for i in hobby][:-1]
except FileNotFoundError:
    print("Файл не был создан")

slovar = {}
i = 0
flag = True

while i < len(users):
    if i >= len(hobby):
        slovar[users[i]] = None
        i += 1
    elif len(hobby) > len(users):
        flag = False
        print('Code 1')
        break
    else:
        slovar[users[i]] = hobby[i]
        i += 1

if flag != False:
    with open("slovar.txt", 'w', encoding='utf-8') as f_slovar:
        f_slovar.write(f'{slovar}')

# 6. Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два скрипта с интерфейсом
# командной строки: для записи данных и для вывода на экран записанных данных. При записи передавать из командной строки
# значение суммы продаж. Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу, по номер, равный второму числу, включительно.
# Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1

# Решение: смотри файлы
# add_sale_py добавить значение в
# show_sales.py показать значения
# edit_sales.py исправить значение по номеру строки
# util.py  модуль с функциями