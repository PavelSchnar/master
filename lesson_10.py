# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы складываем с
# первым элементом первой строки второй матрицы и пр.
import copy


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return '\n'.join(
            ['\t'.join([str(j) for j in i]) for i in self.matrix]
        )

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix):
            return None
        res = copy.deepcopy(self.matrix)
        for i in range(len(self.matrix)):
            for k in range(len(self.matrix[i])):
                res[i][k] = self.matrix[i][k] + other.matrix[i][k]
        return Matrix(res)


list_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
list_2 = [[10, 11, 12], [13, 14, 15], [16, 17, 18]]
matrix_1 = Matrix(list_1)
matrix_2 = Matrix(list_2)

print(matrix_1)
print(matrix_2)

matrix_3 = matrix_1 + matrix_2

print(matrix_3)


# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определённое название. К типам одежды в этом проекте относятся пальто и костюм. У этих
# типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
# соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания. Реализовать абстрактные
# классы для основных классов проекта и проверить работу декоратора @property.

from abc import ABC
from abc import abstractmethod


class Closes(ABC):
    def __init__(self, param):
        self.param = param

    def __str__(self):
        return f'Текущее значение параметра для {self.__class__.__name__} равен {self.param}'

    @abstractmethod
    def rashod_tkani(self):
        pass


class Coat(Closes):

    @property
    def rashod_tkani(self):
        return f'Расход ткани равен {round(self.param / 6.5 + 0.5, 2)}'


class Jacket(Closes):

    @property
    def rashod_tkani(self):
        return round(self.param * 2 + 0.3, 2)


coat = Coat(56.4)
print(coat.rashod_tkani)

jacket = Jacket(55.1)
print(jacket)

# 3. Осуществить программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс «Клетка».
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число). В классе должны
# быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение
# (__mul__()), деление (__floordiv__, __truediv__()). Эти методы должны применяться только к клеткам и выполнять
# увеличение, уменьшение, умножение и округление до целого числа деления клеток, соответственно.

# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.

# Вычитание. Участвуют две клетки. Операцию необходимо выполнять, только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.

# Умножение. Создаётся общая клетка из двух. Число ячеек общей клетки — произведение количества ячеек этих двух клеток.

# Деление. Создаётся общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.

# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Этот метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, а количество ячеек в ряду — 5. В этом случае метод make_order() вернёт
# строку: *****\n*****\n**.
# Или, количество ячеек клетки — 15, а количество ячеек в ряду равняется 5. Тогда метод make_order() вернёт строку:
# *****\n*****\n*****.

class Cell:
    def __init__(self, param_int):
        self.param_int = param_int

    def __str__(self):
        return f'Количество ячеек в клетке равно {self.param_int}'

    def __sub__(self, other):
        return Cell(abs(self.param_int - other.param_int))

    def __mul__(self, other):
        return Cell(self.param_int * other.param_int)

    def __truediv__(self, other):
        return Cell(self.param_int // other.param_int)

    def __floordiv__(self, other):
        return Cell(self.param_int // other.param_int)

    def __add__(self, other):
        return Cell(abs(self.param_int + other.param_int))

    def make_order(self, count):
        res = self.param_int
        while res > 0:
            for k in range(1, count):
                print('*', end='')
                res -= 1
                if res <= 0:
                    break
            print('\n', end='')


a_cell = Cell(33)
b_cell = Cell(11)

print(a_cell)
print(b_cell)
a_cell.make_order(5)
b_cell.make_order(6)

print(a_cell - b_cell)
print(a_cell * b_cell)
print(a_cell / b_cell)
print(a_cell + b_cell)
