# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod. Он должен извлекать число, месяц, год и
# преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и
# года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class Date_time:
    def __init__(self, string_date):
        self.string_date = str(string_date)

    def __str__(self):
        return self.string_date

    @classmethod
    def get_int_values(cls, string_date):
        res = string_date.split('-')
        return int(res[0]), int(res[1]), int(res[2])

    @staticmethod
    def validate_date(stat_date):
        res = [int(i) for i in stat_date.split('-')]
        print(res)
        if res[0] <= 31 and res[0] >= 1:
            if res[1] <= 12 and res[0] >= 1:
                if res[2] <= 2050 and res[2] >= 2020:
                    return f'Дата корректная'
                else:
                    return f'Как минимум некорректный год'
            else:
                return f'Как минимум некорректный месяц'
        else:
            return f'Как минимум некорректный день'


time_obj = Date_time('10-11-2021')
print(time_obj.get_int_values('17-09-2021'))
print(Date_time.get_int_values('17-09-2021'))
print(time_obj.validate_date('12-12-1111'))
print(time_obj.validate_date('11-07-2021'))


#
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль. Проверьте его работу на данных,
# вводимых пользователем. При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.


class My_exception:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @staticmethod
    def div_zero(value1, value2):
        try:
            return (value1 / value2)
        except:
            return (f'Деление на ноль!')


div_ex = My_exception(10, 5)
print(div_ex.div_zero(4, 0))

print(My_exception.div_zero(5, 0))


# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере. Запрашивать у пользователя данные и заполнять список необходимо
# только числами. Класс-исключение должен контролировать типы данных элементов списка.

# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу
# скрипта, введя, например, команду «stop». При этом скрипт завершается, сформированный список с числами выводится на
# экран.
# Подсказка: для этого задания примем, что пользователь может вводить только числа и строки. Во время ввода
# пользователем очередного элемента необходимо реализовать проверку типа элемента. Вносить его в список, только если
# введено число.
# Класс-исключение должен не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

class My_exception_new:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):
        while True:
            try:
                res = int(input('Введите значения и нажимайте Enter - '))
                if type(res) == int:
                    self.my_list.append(res)
                    print(f'текущее значение = {self.my_list}\n')

            except:
                y_or_n = input(f'Похоже веденное значение не число, хотите остановить скрипт? Y/N')
                if y_or_n == 'N' or y_or_n == 'n':
                    print(self.my_input())
                elif y_or_n == 'Y' or y_or_n == 'y':
                    return f'Вы вышли'
                else:
                    return f'Вы все равно вышли'


try_except = My_exception_new(1)
print(try_except.my_input())

# 4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определите параметры, общие для приведённых типов. В классах-наследниках реализуйте параметры,
# уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработайте методы, которые отвечают за приём оргтехники на склад и передачу
# в определённое подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники, а также других
# данных, можно использовать любую подходящую структуру (например, словарь).

# 6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных. Например, для
# указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь реализовать в проекте «Склад оргтехники» максимум возможностей, изученных на уроках по ООП.
class StockEquipment:
    #создадим список- БД для всех устройств
    my_store = []

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists

        my_unit = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}
        StockEquipment.my_store.append(my_unit)

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    @classmethod
    def currentstatus(cls):
        print(f'Текущий список -\n {cls.my_store}')

    @classmethod
    def reception(cls):

        try:
            unit = input(f'Введите наименование ')
            unit_p = int(input(f'Введите цену за ед '))
            unit_q = int(input(f'Введите количество '))
            unique = {'Модель устройства': unit, 'Цена за ед': unit_p, 'Количество': unit_q}

            cls.my_store.append(unique)
            print(f'Текущий список -\n {cls.my_store}')
        except:
            return f'Ошибка. При вводе данных укажите число'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            print(f'Весь склад -\n {cls.my_store}')
            return f'Выход'
        else:
            return StockEquipment.reception()


class Printer(StockEquipment):
       def to_print(self):
        return f'to print smth {self.numb} times'


class Scanner(StockEquipment):
    def to_scan(self):
        return f'to scan smth {self.numb} times'


class Copier(StockEquipment):
    def to_copier(self):
        return f'to copier smth  {self.numb} times'


printerUnit = Printer('hp', 2000, 5, 10)
StockEquipment.currentstatus()
scannerUnit = Scanner('canon', 2002, 51, 12)
StockEquipment.currentstatus()
copierUnit = Copier('konica', 2004, 53, 10)
StockEquipment.currentstatus()

StockEquipment.reception()



# 7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число». Реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта. Для этого создаёте экземпляры класса
# (комплексные числа), выполните сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.
class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -2)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)