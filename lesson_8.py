# 1. Написать функцию email_parse(<email_address>), которая при помощи регулярного выражения извлекает имя пользователя
# и почтовый домен из email адреса и возвращает их в виде словаря. Если адрес не валиден, выбросить исключение
# ValueError.
# Пример:
# >>> email_parse('someone@geekbrains.ru')
# {'username': 'someone', 'domain': 'geekbrains.ru'}
# >>> email_parse('someone@geekbrainsru')
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   ...
#     raise ValueError(msg)
# ValueError: wrong email: someone@geekbrainsru
# Примечание: подумайте о возможных ошибках в адресе и постарайтесь учесть их в регулярном выражении; имеет ли смысл в
# данном случае использовать функцию re.compile()?

# !!!!!!!!!!!!!!
# Компиляция может способствовать повышению быстродействия приложения. Однако, скомпилированные версии недавно
# использованных регулярных выражений кешируются, поэтому программам, использующим небольшое количество выражений, можно
# не вызывать их компиляцию явно.

import re


def email_parse(email):
    result = {}
    if re.fullmatch(regex, email):
        print("Valid email")
        match = re.search(regex, email)
        result['username'] = match.group(1)
        result['domain'] = match.group(3)
        print(result)

    else:
        raise ValueError('wrong email:', email)


regex = re.compile(r'(([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+)@([A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+)')
mail = "pavel.regex.copypast@yandex.com"

email_parse(mail)

# 3. Написать декоратор для логирования типов позиционных аргументов функции, например:
# def type_logger...
#     ...
#
#
# @type_logger
# def calc_cube(x):
#    return x ** 3
#
# >>> a = calc_cube(5)
# 5: <class 'int'>
# Примечание: если аргументов несколько - выводить данные о каждом через запятую; можете ли вы вывести тип значения
# функции? Сможете ли решить задачу для именованных аргументов? Сможете ли вы замаскировать работу декоратора?
# Сможете ли вывести имя функции, например, в виде:
# >>> a = calc_cube(5)
# calc_cube(5: <class 'int'>)


def type_logger(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f'{arg}: {type(arg)}')
        for kwarg in kwargs:
            print(f'{kwargs[kwarg]}: {type(kwargs[kwarg])}')

    return wrapper


def func_type():
    pass


@type_logger
def calc_cube(x):
    return x ** 3


b = func_type
a = calc_cube(5, 3, '234', b, c=6)

# 4. Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные значения функции и выбрасывать
# исключение ValueError, если что-то не так, например:
# def val_checker...
#     ...
#
#
# @val_checker(lambda x: x > 0)
# def calc_cube(x):
#    return x ** 3
#
#
# >>> a = calc_cube(5)
# 125
# >>> a = calc_cube(-5)
# Traceback (most recent call last):
#   ...
#     raise ValueError(msg)
# ValueError: wrong val -5


def val_checker(func):
    def wrapper(x):
        if x <= 0:
            raise ValueError(f'wrong val {x}')
        else:
            a = func(x)
            print(a)

    return wrapper


@val_checker
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
