# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?); как лучше хранить конфигурацию
# этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект; можно ли будет при этом расширять
# конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os
from pathlib import Path
import shutil


def create_folder(path):
    if not os.path.exists(path):
        path.mkdir(parents=True, exist_ok=True)


def create_file(root, file_name):
    with open(Path(f'{root}/{file_name}'), 'w'):
        pass


def build_structure(root, data):
    if data:
        for k, v in data.items():
            folder_name = k
            folder_path = Path(f'{root}/{folder_name}')

            create_folder(folder_path)

            for elem in v:
                if not isinstance(elem, dict):
                    create_file(folder_path, elem)
                elif isinstance(elem, dict):
                    build_structure(folder_path, elem)


structure = {
    'settings':
        ['__init__.py', 'dev.py', 'prod.py'],
    'mainapp':
        ['__init__.py', 'models.py', 'views.py',
         {'templates':
              [{'mainapp':
                    ['base.html', 'index.html']
                }]
          }
         ],
    'authapp':
        ['__init__.py', 'models.py', 'views.py',
         {'templates':
              [{'authapp':
                    ['base.html', 'index.html']
                }]
          }
         ]
}

# каталог root
dir_ = os.path.abspath(os.curdir)

# Название проекта
projectname = 'my_project'

# Путь до проекта
project_path = Path(f'{dir_}/{projectname}')

# Создаём папку с проектом
create_folder(project_path)

# Создаем заготовку
build_structure(project_path, structure)


# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание, что html-файлы расположены в родительских папках
# (они играют роль пространств имён); предусмотреть возможные исключительные ситуации; это реальная задача, которая
# решена, например, во фреймворке django.

def copytree(src, dst, symlinks=False, ignore=None):
    try:
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)
    except FileExistsError:
        print('File already copied and exist')


def copy_folders(path, folder_name):
    new_folder_name = folder_name
    new_folder_path = Path(f'{project_path}/{new_folder_name}')
    create_folder(new_folder_path)
    for root, dirs, files in os.walk(path):
        for d in dirs:
            if d == folder_name:
                copytree(f'{root}/{d}', new_folder_path)


copy_folders(project_path, 'templates')

# 4. Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором ключи — верхняя граница
# размера файла (пусть будет кратна 10), а значения — общее количество файлов (в том числе и в подпапках), размер
# которых не превышает этой границы, но больше предыдущей (начинаем с 0), например:
#     {
#       100: 15,
#       1000: 3,
#       10000: 7,
#       100000: 2
#     }
# Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
# Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.


new_path = Path(f"{dir_}/venv")
slovar = {'100': 0, '1000': 0, '10000': 0, '100000': 0}

for root, dirs, files in os.walk(new_path):
    count_100 = 0
    count_1000 = 0
    count_10000 = 0
    count_100000 = 0
    for file in files:
        size = os.stat(root).st_size
        if size < 100:
            count_100 += 1
            slovar['100'] = count_100

        elif size >= 100 and size < 1000:
            count_1000 += 1
            slovar['1000'] = count_1000

        elif size >= 10000 and size < 100000:
            count_10000 += 1
            slovar['10000'] = count_10000

        elif size >= 100000:
            count_100000 += 1
            slovar['100000'] = count_100000

print(slovar)
