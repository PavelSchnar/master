FILENAME = 'bakery.csv'

def add_sales(value):
    with open(FILENAME, 'a', encoding='utf-8') as file:
        file.write(f'{value}\n')


def show_sales(value1=None, value2=None):
    with open(FILENAME, 'r', encoding='utf-8') as file:
        res = file.read()
        temp = res.split('\n')[:-1]

        if value1 != None and value2 == None:
            for i in temp[value1 - 1:]:
                print(i)
        elif value2 != None:
            for i in temp[value1 - 1:value2]:
                print(i)
        elif value1 == None and value2 == None:
            print(res)


def edit_sales(number, new_val):
    with open(FILENAME, 'r', encoding='utf-8') as file:
        line = file.readlines()
    if number <= len(line):
        with open(FILENAME, 'w', encoding='utf-8') as file:
            line[number - 1] = f'{new_val}\n'
            file.writelines(line)
    else:
        print(f'Строки с номером {number} не существует, всего {len(line)} строк')



