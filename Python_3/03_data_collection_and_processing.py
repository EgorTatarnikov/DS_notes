#_____ Data Collection and Processing with Python _____#

    # Nested Data (вложенные структуры данных) в Python

# Вложенные данные — это структуры данных, содержащие другие структуры:
# списки в списках, словари в словарях, списки в словарях и т.д.

# ▶ Примеры вложенных структур:

# Список списков:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Словарь списков:
student_scores = {
    "Alice": [85, 90, 95],
    "Bob": [78, 82, 88]
}

# Список словарей:
users = [
    {"id": 1, "name": "Egor"},
    {"id": 2, "name": "Yeva"}
]

# Словарь словарей:
user_profiles = {
    "egor": {"age": 30, "city": "Korolev"},
    "yeva": {"age": 25, "city": "Moscow"}
}

# ▶ Доступ к данным:

# Элемент во вложенном списке:
element = matrix[1][2]  # 6

# Оценка Боба:
score = student_scores["Bob"][1]  # 82

# Имя второго пользователя:
name = users[1]["name"]  # "Yeva"

# Город Егора:
city = user_profiles["egor"]["city"]  # "Korolev"


# ▶ Итерация по вложенным структурам:

# Перебор матрицы:
for row in matrix:
    for value in row:
        print(value)

# Перебор списка словарей:
for user in users:
    print(user["name"])

# Перебор списка списков:
nested = [['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested:
    print("level1: ")
    for y in x:
        print("     level2: " + y)

# Пример 1 : список с разным уровнем вложенности
nested1 = [1, 2, ['a', 'b', 'c'],['d', 'e'],['f', 'g', 'h']]
for x in nested1:
    print("level1: ")
    if type(x) is list:
        for y in x:
            print("     level2: {}".format(y))
    else:
        print(x)

# Пример 2 : список с разным уровнем вложенности (любой сложности)  
data = [
    1,
    [2, 3],
    [[4, 5], 6],
    7,
    [[[8]]]
]

def iterate_nested(lst):
    for item in lst:
        if isinstance(item, list):
            # если элемент — список, рекурсивно итерируем внутри
            yield from iterate_nested(item)
        else:
            yield item

for value in iterate_nested(data):
    print(value, end=' ')
print()


# ▶ Изменение вложенных данных:

# Изменим значение:
matrix[0][1] = 42
users[0]["name"] = "Yegor"

# ▶ Практические приёмы:

# Добавление элемента:
student_scores["Alice"].append(100)

# Проверка существования ключа:
if "egor" in user_profiles:
    print(user_profiles["egor"]["age"])




    # *args и **kwargs в Python

# знаки * и ** в пайтоне используются для распаковки аргументов при вызове функций
# * — распаковывает итерируемый объект (список, кортеж, строку и т.п.). Передаёт его элементы как позиционные аргументы.
# ** — распаковывает словарь. Передаёт его пары ключ=значение как именованные аргументы.
# ▶ Распаковка аргументов:
numbers = [10, 20, 30]
params = {"sep": " | "}
print(*numbers, **params)  # 10 | 20 | 30

# ▶ *args — собирает произвольное количество позиционных аргументов в кортеж
# *args — нужен, чтобы передавать любое количество позиционных аргументов в функцию.
# Полезно, когда ты не знаешь заранее, сколько аргументов будет передано.
def example_args(*args):
    print(args)

example_args(1, 2, 3)  # (1, 2, 3)

# ▶ **kwargs — собирает произвольное количество именованных аргументов в словарь
# **kwargs — нужен, чтобы передавать любое количество именованных аргументов (в виде ключ=значение).
# Удобно для настройки параметров или прокидывания аргументов в другие функции
def example_kwargs(**kwargs):
    print(kwargs)

example_kwargs(name="Egor", age=30)  # {'name': 'Egor', 'age': 30}

# ▶ Использование вместе:
def example_all(*args, **kwargs):
    print("args:", args)
    print("kwargs:", kwargs)

example_all(1, 2, name="Yeva", job="AI")  
# args: (1, 2)
# kwargs: {'name': 'Yeva', 'job': 'AI'}




    #  Работа с JSON в Python (модуль json)

# JSON (JavaScript Object Notation) — текстовый формат хранения структурированных данных.
# Широко используется для обмена данными между приложениями, особенно в API и веб-разработке.

# Пример JSON:
# {
#     "name": "Egor",
#     "age": 30,
#     "skills": [
#         "Python", 
#         "Machine Learning"
#     ]
# }

# Модуль json (встроенный модуль Python) нужен для работы с форматом JSON
import json

# Основные функции: 
# dump, dumps - Конвертация Python-объектов в JSON (сериализация)
# load, loads -  Парсинг JSON-строк в Python-объекты (десериализация)

# 🔹 Функция json.dumps(obj, **kwargs)
# Преобразует Python-объект (словарь, список и т.д.) в JSON-строку (str).

data = {
    "name": "Egor",
    "age": 30,
    "skills": ["Python", "Data Science"]
}

json_string = json.dumps(data)
print(json_string)  # '{"name": "Egor", "age": 30, "skills": ["Python", "Data Science"]}'

# С отступами и читаемым форматом:
pretty_json = json.dumps(data, indent=4, ensure_ascii=False)    
# indent добавляет отступы. Без этого параметра JSON будет в одной строке
# ensure_ascii=False - Unicode (в том числе русские) символы сохранятся в читаемом виде, а не в в \uXXXX
print(pretty_json)
# {
#     "name": "Egor",
#     "age": 30,
#     "skills": [
#         "Python", 
#         "Machine Learning"
#     ]
# }

# --------------------------------------------
# 🔹 Функция json.loads(json_string)
# Преобразует JSON-строку обратно в Python-объект.

parsed_data = json.loads(json_string)
print(parsed_data["name"])  # "Egor"

# --------------------------------------------
# 🔹 Функция json.dump(obj, file, **kwargs)
# Записывает Python-объект в файл в формате JSON.

with open("./files/data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4, ensure_ascii=False)

# --------------------------------------------
# 🔹 Функция json.load(file)
# Считывает JSON из файла и возвращает Python-объект.

with open("./files/data.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(loaded_data["skills"])

# --------------------------------------------
# 🔹 Таблица соответствия типов данных:

# Python тип          →  JSON тип           →  Пример Python          →  Пример JSON
# ------------------------------------------------------------------------------
# dict                →  объект (object)     →  {"key": "value"}       →  { "key": "value" }
# list, tuple         →  массив (array)      →  [1, 2, 3]              →  [1, 2, 3]
# str                 →  строка (string)     →  "Hello"                →  "Hello"
# int, float          →  число (number)      →  42, 3.14               →  42, 3.14
# True                →  true                →  True                   →  true
# False               →  false               →  False                  →  false
# None                →  null                →  None                   →  null
# --------------------------------------------

# Важные моменты:
# - Ключи словаря (dict) должны быть строками, иначе при сериализации будет ошибка.
#   Например, {10: "val"} вызовет ошибку при сериализации.
# - Кортежи (tuple) сериализуются как списки JSON.
# - Неподдерживаемые типы (например, set, объекты классов) требуют кастомной сериализации.




    # Deep and Shallow Copies

# 🔹 Поверхностное копирование (shallow copy):
# Копируется только верхний уровень объекта.
# Вложенные объекты остаются ссылками на те же самые данные.

import copy

original = [[1, 2], [3, 4]]     # В памяти создаётся внешний список и два вложенных списка.
shallow = copy.copy(original)   # поверхностная копия (shallow). Создается новый внешний список, но внутренние списки остаются общими (указывают на те же объекты)
shallow_2 = original[:]         # тоже способ поверхностного копирования. Срез копирует только верхний уровень

original[0][0] = 99             # Меняется первый элемент первого вложенного списка. Этот вложенный список общий для всех копий → изменение отразится везде.
shallow_2[1] = [10, 11]         # Мы заменяем второй вложенный список в shallow_2. Это разрывает связь с original[1] → теперь shallow_2[1] указывает на новый список, независимый.
print(original)                 # [[99, 2], [3, 4]] - изменился оригинал
print(shallow)                  # [[99, 2], [3, 4]] - и копия
print(shallow_2)                # [[99, 2], [10, 11]] - вторая вложенность заменена, первая всё ещё ссылается на общий объект

# 🔹 Глубокое копирование (deep copy):
# Копируются все уровни, включая вложенные объекты.
# Результат — полностью независимая копия.

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)  # глубокая копия (deep)

deep[0][0] = 99
print(original)                 # [[1, 2], [3, 4]] — оригинал не изменился




    # Map, Filter, List Comprehensions, and Zip

# --- Функция map() ---
# Сигнатура: map(function, iterable)
# Применяет функцию к каждому элементу списка и возвращает ИТЕРАТОР (не список!)
# Чтобы увидеть результат — нужно обернуть в list()

nums = [1, 2, 3, 4]

# Пример 1: lambda-функция
print(list(map(lambda x: 2 * x, nums)))  # [2, 4, 6, 8]

# Пример 2: именованная функция
def double(x):
    return x * 2

print(list(map(double, nums)))          # [2, 4, 6, 8]

# Без map — тот же эффект вручную:
def doubleStuff(a_list):
    new_list = []
    for value in a_list:
        new_elem = double(value)
        new_list.append(new_elem)
    return new_list

print(doubleStuff(nums))                # [2, 4, 6, 8]


# --- Функция filter() ---
# Сигнатура: filter(function, iterable)
# Возвращает итератор из элементов, для которых функция возвращает True.
# Чтобы увидеть результат — нужно обернуть в list()

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 
             'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
print(list(filter(lambda x: 'B' in x, countries)))  # ['Brazil', 'Botswana', 'Britain', 'Belarus', 'Belgium']

nums = [1, 2, 3, 4, 5]

# Пример 1: lambda-функция
print(list(filter(lambda x: x % 2 != 0, nums)))  # [1, 3, 5]

# Пример 2: именованная функция
def is_odd(x):
    return x % 2 != 0

print(list(filter(is_odd, nums)))                # [1, 3, 5]

# Без filter — вручную:
def filter_odds(a_list):
    result = []
    for x in a_list:
        if is_odd(x):
            result.append(x)
    return result

print(filter_odds(nums))                         # [1, 3, 5]


# --- Функция zip() ---
# Сигнатура: zip(iter1, iter2, ...)
# Объединяет элементы из нескольких списков в кортежи
# Чтобы увидеть результат — нужно обернуть в list()

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

# Пример 1: объединение списков
print(list(zip(names, ages)))  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Пример 2: распаковка
zipped = list(zip(names, ages))
print(zipped)                   # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
# * перед zipped распаковывает список кортежей в отдельные аргументы: zip(('Alice', 25), ('Bob', 30), ('Charlie', 35))
# затем zip(...) группирует по позициям внутри кортежей:
print(list(zip(*zipped)))   # [('Alice', 'Bob', 'Charlie'), (25, 30, 35)]
# далее кортеж списков распаковывается в unzipped_names, unzipped_ages
unzipped_names, unzipped_ages = zip(*zipped)
print(unzipped_names)          # ('Alice', 'Bob', 'Charlie')
print(unzipped_ages)           # (25, 30, 35)

# Пример 3: списки разной длины
a = [1, 2, 3]
b = ['a', 'b']
print(list(zip(a, b)))         # [(1, 'a'), (2, 'b')]

# Без zip — вручную:
def manual_zip(list1, list2):
    result = []
    for i in range(min(len(list1), len(list2))):
        result.append((list1[i], list2[i]))
    return result

print(manual_zip(a, b))        # [(1, 'a'), (2, 'b')]


# --- List Comprehension ---
# полностью заменяет map и filter
# Сигнатура: [expression for item in iterable if condition (опционально)]
# Возвращает List

# Пример 1: квадраты чисел
print([x**2 for x in range(5)])          # [0, 1, 4, 9, 16]

# Пример 2: только чётные
print([x for x in range(10) if x % 2 == 0])  # [0, 2, 4, 6, 8]

# Пример 3 с zip 
L1 = [1, 5, 2, 16, 32, 3, 54, 8, 100]
L2 = [1, 3, 10, 2, 42, 2, 3, 4, 3]
L3 = [x + y for (x, y) in list(zip(L1, L2)) if (x > 10 and y < 5)]
print(L3)   # [18, 57, 103]

# Пример 4: аналог filter + map
print([x**2 for x in nums if x % 2 == 0])    # [4, 16]

# Без list comprehension — обычный цикл:
def squared_evens(a_list):
    result = []
    for x in a_list:
        if x % 2 == 0:
            result.append(x ** 2)
    return result

print(squared_evens(nums))                  # [4, 16]


# Пример. Составить список вымирающих видов.
species = [
    'golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel',
    'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout',
    'black bear', 'blue whale', 'water moccasin', 'giant panda',
    'green turtle', 'blue jay', 'japanese beetle'
]

population = [
    10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000,
    12000, 2300, 7500, 100, 1800, 9500, 125000
]

# Шаг 1: Объединить в пары (вид, популяция)
pop_info = list(zip(species, population))

# Шаг 2: Оставить только тех, у кого популяция < 2500
endangered = [name for name, pop in pop_info if pop < 2500]

print(endangered)   # ['black rhino', 'orangutan', 'sumatran elephant', 'blue whale', 'giant panda', 'green turtle']




    # Data Parsing HTML / веб-страниц

# Модуль requests в Python — это мощная и удобная библиотека для работы с HTTP-запросами. С его помощью можно легко:
# - скачивать страницы с интернета,
# - отправлять GET и POST-запросы,
# - работать с API.

import requests
import json

page = requests.get("https://api.datamuse.com/words?rel_rhy=funny")
print(type(page))
print(page.text[:150]) # print the first 150 characters
print(page.url) # print the url that was fetched
print("------")
x = page.json() # turn page.text into a python object
print(type(x))
print("---first item in the list---")
print(x[0])
print("---the whole list, pretty printed---")
print(json.dumps(x, indent=2)) # pretty print the results


iTunes_response = requests.get("https://itunes.apple.com/search?term=jack+johnson&media=music&entity=musicTrack&limit=25")
py_data = json.loads(iTunes_response.text)
for r in py_data['results']:
    print(r['trackName'])




    # Для справки

    # yield и return

# return — возвращает значение и завершает функцию
def f():
    return 1
    print("Это не выполнится")

print(f())  # 1

# yield — возвращает значение во временной точке и приостанавливает функцию
# Функция с yield — это генератор. Она возвращает значения по одному, сохраняя своё состояние, и может быть возобновлена позже.
# Функция с yield — это генератор, и она завершается, когда выполнение достигает конца функции или встречает return без значения.
def gen():
    yield 1
    yield 2
    yield 3

g = gen()
print(next(g))  # 1
print(next(g))  # 2
print(next(g))  # 3


    # yield from — делегирование генератора

# Обычный генератор возвращает значения через yield:

def gen1():
    yield 1
    yield 2

def gen2():
    yield 3
    yield 4

# Чтобы вывести все значения из gen1 и gen2, можно делать так:

def combined_old():
    for v in gen1():
        yield v
    for v in gen2():
        yield v

# Но это громоздко. Вместо этого есть удобный синтаксис:

def combined_new():
    yield from gen1()   # делегируем генератор gen1()
    yield from gen2()   # делегируем генератор gen2()

# Использование:

for val in combined_new():
    print(val)
# Вывод:
# 1
# 2
# 3
# 4