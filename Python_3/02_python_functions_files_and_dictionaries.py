#_____ Python Functions, Files, and Dictionaries _____#

    # ___ Files ___#
    
    # File Path Examples

# 'example.txt'        – файл в текущей директории
# './example.txt'      – то же самое: текущая директория
# 'files/data.txt'     – файл в подпапке 'files'
# './files/data.txt'   — то же самое, что 'files/data.txt'
# '../data.txt'        – файл на один уровень выше
# '../files/data.txt'  – файл в папке 'files', которая находится уровнем выше
# '/home/user/file.txt'  – абсолютный путь (Linux/macOS)
# 'C:\\Users\\User\\file.txt'  – абсолютный путь (Windows, экранированные слэши)
# r'C:\Users\User\file.txt'  – абсолютный путь (Windows, raw-строка без экранирования)


    # File Open Modes
    
my_file =  open('./files/example_read.txt', 'r', encoding='utf-8')   
print(my_file.read())
print(len(my_file.read()))  # 0 - выводит 0 потому что файл уже прочитан
my_file.seek(0)
print(len(my_file.read()))  # 485
my_file.seek(0)
print(len(my_file.readlines()))
my_file.seek(0)
#for line in my_file.readlines():   # без разницы
for line in my_file:                #   можно и так
    print(line, end='')             # не добавляем лишний \n
my_file.close()

filename = "./files/squared_numbers.txt"
outfile = open(filename, "w")
for number in range(1, 10):
    square = number * number
    outfile.write(str(square) + "\n")
outfile.close()

infile = open(filename, "r")
print(infile.read())
infile.close()

# Using with for Files
# Конструкция with автоматически закрывает файл после завершения блока
# и визуально отделяет блок работы с файлом
# Это предпочтительный способ работы с файлами

# 'r' – read (Чтение. Ошибка, если файл не существует)
# 'utf-8' – универсальная кодировка, которая поддерживает русский, английский и большинство других языков.
# Рекомендуется всегда указывать encoding.
with open('files/example_read.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print(content)

# 'w' – write (Перезаписывает файл. Создаёт, если не существует)
with open('./files/example_write.txt', 'w', encoding='utf-8') as file:
    file.write('Новая строка\n')

# 'a' – append (Добавляет в конец файла. Создаёт, если не существует)
with open('./files/example_append.txt', 'a', encoding='utf-8') as file:
    file.write('Добавленная строка\n')

# 'x' – exclusive creation (Создаёт новый файл. Ошибка, если уже существует.
# with open('./files/example_create.txt', 'x', encoding='utf-8') as file:
#     file.write('Создаём файл впервые')

# 'r+' – чтение + запись (Ошибка, если файл не существует)
with open('./files/example_read_write.txt', 'r+', encoding='utf-8') as file:
    old_content = file.read()
    file.seek(0)  # переместиться в начало файла
    file.write('Новое начало\n' + old_content)

# 'w+' – запись + чтение (Перезаписывает файл или создаёт)
with open('./files/example_write_read.txt', 'w+', encoding='utf-8') as file:
    file.write('Сначала запись\n')
    file.seek(0)
    print(file.read())  # Считаем то, что только что записали

# 'a+' – добавление + чтение (Создаёт файл, если не существует)
with open('./files/example_append_read.txt', 'a+', encoding='utf-8') as file:
    file.write('Строка для добавления\n')
    file.seek(0)
    print(file.read())  # Покажет весь файл, включая добавленное

# 'rb' – чтение в бинарном режиме
with open('./files/example_binary.jpg', 'rb') as file:
    binary_data = file.read()
    print(type(binary_data))  # <class 'bytes'>

# 'wb' – запись в бинарном режиме
with open('./files/example_copy.jpg', 'wb') as file:
    file.write(binary_data)
    
    
    # File Object Methods
    
# write(astring) – записывает строку в файл
with open('./files/methods_write.txt', 'w', encoding='utf-8') as file:
    file.write('Привет, мир!\n')
    file.write('Это вторая строка.\n')

# read(n) – читает n символов или весь файл, если n не указан
with open('./files/methods_write.txt', 'r', encoding='utf-8') as file:
    full_text = file.read()  # читаем всё
    print(full_text)

# readline() – читает одну строку (до \n)
with open('./files/methods_write.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    print('Первая строка:', first_line)

# readlines() – читает все строки в список
with open('./files/methods_write.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    print('Список строк:', lines)

# writelines(list_of_strings) – записывает список строк в файл
lines_to_write = ['строка 1\n', 'строка 2\n', 'строка 3\n']
with open('./files/methods_writelines.txt', 'w', encoding='utf-8') as file:
    file.writelines(lines_to_write)

# seek(offset) – перемещает указатель позиции (в байтах)
with open('./files/methods_write.txt', 'r', encoding='utf-8') as file:
    file.seek(4)  # перейти на 4-й байт
    print(file.read(10))  # читаем 10 символов с позиции 5

# tell() – показывает текущую позицию указателя
with open('./files/methods_write.txt', 'r', encoding='utf-8') as file:
    file.seek(4)  # перейти на 4-й байт
    print('Позиция в начале:', file.tell())                 # 4
    file.read(7)
    print('Позиция после чтения 7 символов:', file.tell())  # 16, потому что в 'utf-8' буквы - 2 байта, а ',' и ' ' - 1 байт

# flush() – принудительно записывает буфер в файл (обычно используется с 'w')
with open('./files/methods_flush.txt', 'w', encoding='utf-8') as file:
    file.write('Буфер записан.\n')
    file.flush()  # полезно при долгой работе с файлами
    
# Если файл большой, лучше читать его построчно в цикле:
with open('./files/bigfile.txt', 'r', encoding='utf-8') as file:
    for line in file:
        print(line.strip())  # strip удаляет \n в конце строки
      


    # ___ Работа с CSV файлами в Python ___ #

olympians = [("John Aalberg", 31, "Cross Country Skiing"),
             ("Minna Maarit Aalto", 30, "Sailing, 1500m"), # csv.writer бере
             ("Win Valdemar Aaltonen", 54, "Art Competitions"),
             ("Wakako Abe", 18, "Cycling")]

writer = open("./files/my_file.csv", 'w')
for olympian in olympians:
    writer.write(f"{olympian[0]},{olympian[1]},{olympian[2]}")
    writer.write('\n')
writer.close()
  

import csv

csvfile = open("./files/my_file.csv", 'w', newline='')
writer = csv.writer(csvfile)
writer.writerow(['Name', 'Age', 'Sport'])
for olympian in olympians:
    writer.writerow(olympian)
csvfile.close()

# Пример 1: чтение CSV как список списков
with open('files/data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)  # ['name', 'age'], затем ['Egor', '32'], ['Anna', '28']

# Пример 2: чтение CSV как словари
with open('files/data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['age'])  # Egor 32, затем Anna 28

# Пример 3: запись в CSV (список списков)
# newline='' в open() предотвращает появление лишних пустых строк в CSV-файле. Это касается только записи. 
with open('files/output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['name', 'age'])      # заголовки
    writer.writerow(['Egor', 32])         # строка 1
    writer.writerow(['Anna', 28])         # строка 2
# output.csv будет выглядеть так:
# name,age
# Egor,32
# Anna,28

# Пример 4: запись в CSV (список словарей)
with open('files/output_dict.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({'name': 'Egor', 'age': 32})
    writer.writerow({'name': 'Anna', 'age': 28})
# output_dict.csv будет иметь такой же результат, но создан с использованием словарей



    # ___ Dictionaries ___ #

# Словарь — это изменяемая структура данных, где значения хранятся в паре ключ:значение
# ключом в словаре может быть только неизменяемый объект

# Создание словаря
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Доступ к значениям
print(person["name"])  # Alice

# Добавление и изменение элементов
person["job"] = "Engineer"
person["age"] = 31

# Удаление элементов
del person["city"]         # Удаление по ключу
print(person.pop("job"))   # Возврат и удаление значения (Engineer)

print(person)   # {'name': 'Alice', 'age': 31}


# Получение значения
print(person.get('age'))    # 31
print(person.get('job'))    # None
# Безопасное получение значения
print(person.get("city", "Not found"))  # Вернет "Not found", если ключа нет

# Проверка наличия ключа
print('age' in person)  # True

if "name" in person:
    print("Name is present")
else:
    print("There is no name")
    
# Получение всех ключей, значений и пар
print(person.keys())    # dict_keys(['name', 'age'])
print(person.values())  # dict_values(['Alice', 31])
print(person.items())   # dict_items([('name', 'Alice'), ('age', 31)])

# list() — это встроенная функция в Python, преобразует переданный ей объект в список, если это возможно.
print(list(person.keys()))      # ['name', 'age']
print(list(person.values()))    # ['Alice', 31]
print(list(person.items()))     # [('name', 'Alice'), ('age', 31)]

#print(person.keys()[0])        # TypeError
print(list(person.keys())[0])   # name
# Очистка словаря
#person.clear()
#print(person)   # {}

# Копирование словаря
wrong_copy = person
print(hex(id(person)))      # 0x2a61d957980
print(hex(id(wrong_copy)))  # 0x2a61d957980 - скопировали только ссылку на словарь
person_copy = person.copy()
print(hex(id(person)))      # 0x2a61d957980
print(hex(id(person_copy))) # 0x2a61da10400 - адрес поменялся

# Объединение словарей (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2 
print(merged) # {'a': 1, 'b': 2}

# Итерация по словарю

# По ключам
for key in person.keys():
    print(f"Key: {key}, Value: {person[key]}")
# можно и так, то же самое
for key in person:
    print(f"Key: {key}, Value: {person[key]}")
    
# По значениям
for value in person.values():
    print(f"Value: {value}")

# По парам ключ-значение
for key, value in person.items():
    print(f"{key} -> {value}")
    
# Пример: подсчёт частоты символов
text = "banana"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1  # если буквы еще нет, создает новый ключ, возвращает 0 и прибавляет 1, 
                                        # если буква уже есть возвращает сколько уже насчитал и прибавляет 1
print(freq)  # {'b': 1, 'a': 3, 'n': 2}

text = "London is the capital of the United Kingdom"
dict_char = {}
for c in text:
    if c not in dict_char:
        dict_char[c] = 0
    dict_char[c] += 1
print(dict_char)

dict_words = {}
for word in text.split():
    if word not in dict_words:
        dict_words[word] = 0
    dict_words[word] += 1
print(dict_words)



# Работа с CSV-файлами через DictReader и DictWriter
import csv

# Чтение CSV через DictReader
# Каждая строка файла превращается в словарь: ключи — из заголовков CSV

with open('./files/data.csv', mode='r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # пример: {'name': 'Alice', 'age': '30'}

# апись в CSV через DictWriter
# Сначала указываем список полей (заголовков)

fieldnames = ['name', 'age', 'city']
data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'London'}
]

with open('./files/output.csv', mode='w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()        # Запись заголовков
    writer.writerows(data)      # Запись всех строк сразу
    # Или:
    # for row in data:
    #     writer.writerow(row)

# Полезно знать
# - DictReader автоматически преобразует первую строку файла в ключи словаря
# - DictWriter требует вручную указать fieldnames
# - Используйте newline='' при работе с файлами на Windows
# - Все значения читаются как строки — для чисел нужна дополнительная обработка



    # ___ Functions ___#

# The syntax for creating a named function, a function definition, is:
# def name(parameters):
#     """documentation"""   # необязательно
#     statements
#     return result
# параметры и return необязательны. Если return нет возвращается None

# A type annotation
def add(x: int, y: int) -> int:         # A type annotation. Показывает какие данные должны быть переданы в функцию 
                                        # и какие она возвращает. Не обязательна к исполнению.
    """Returns the sum of `x` and `y`"""
    return x + y

# Локальные и глобальные переменные
power = 2                   # power - глобальная переменная
def my_square(x):           # x - локальная переменная
    y = x ** power          # можно ссылаться на глобальные переменные. так делать плохо, но можно
                            # к примеру можно сослаться на констану.
    return y

def my_power(x, power):     # x, power - локальные переменные
    y = x ** power          # сначала пайтон будет искать локальные переменные, а если не найдет - глобальные
    return y

print(my_square(10))    # 100
print(my_power(10,3))   # 1000


    # Passing Mutable Objects
# В Python переменные — это ссылки на объекты.
# Мы не можем изменить саму переменную (ссылку), переданную в функцию,
# но можем изменить содержимое изменяемого объекта (например, список, словарь и т.д.).

# Пример с изменяемым объектом:
def modify_list(lst):   # локальная переменная lst ссылается на тот же список, что и глобальная my_list.
    lst.append(42)      # меняется сам объект

my_list = [1, 2, 3]
modify_list(my_list)
print(my_list)  # [1, 2, 3, 42] — список изменился
modify_list(list(my_list))  # list() делаем копию списка
print(my_list)  # [1, 2, 3, 42] — список неизменился

# Пример с неизменяемым объектом:
def try_modify(x):
    x += 10  # создаётся новый объект, исходный не меняется

a = 5
try_modify(a)
print(a)  # 5 — переменная a осталась без изменений

# Пример с изменяемым объектом (нюанс):
def changeit(lst):
    lst = ["Michigan", "Wolverines"]  # создаётся НОВЫЙ список и локальная переменная lst нереназначается на него.

mylst = ['our', 'students', 'are', 'awesome']
changeit(mylst)
print(mylst)  # ['our', 'students', 'are', 'awesome']


# Параметр (parameter) - это имя переменной, указанное в определении функции.
#                       A name used inside a function to refer to the value which was passed to it as an argument.
# Аргумент (argument) — это конкретное значение, которое передаётся функции при вызове.
#                       A value provided to a function when the function is called.



    # Проверка функций с помощью assert

# Проверка типов с помощью assert
def greet(name):
    # assert type(name) == str, "Аргумент 'name' должен быть строкой"
    # assert isinstance(name, str), "Аргумент 'name' должен быть строкой"
    # лучше использовать isinstance(name, str), так как он поддерживает наследование. То есть наследующие объекты тоже пройдут проверку
    print(f"Привет, {name}!")

greet("Егор")      # OK
greet(123)         # AssertionError: Аргумент 'name' должен быть строкой


# Проверка вывода функции через assert
def square(x):
    return x*x
# граничные случаи и любой другой
assert square(1) == 1
assert square(0) == 0
assert square(-1) == 1
assert square(3) == 9

# проверка изменения функцией изменяемых объектов через assert
def update_counts(letters, counts_d):
    for c in letters:
        if c in counts_d:
            counts_d[c] += 1
        else:
            counts_d[c] = 1
            
counts = {'a': 3, 'b': 2}
update_counts("aaab", counts)

assert counts['a'] == 6  # было 3, добавили ещё 3
assert counts['b'] == 3  # было 2, добавили 1

# Testing Optional Parameters
def count_long_words(words, min_length=5):
    ct = 0
    for word in words:
        if len(word) >= min_length:
            ct += 1
    return ct

test_words = ["", "1", "12", "123", "1234", "12345", "123456"]
assert count_long_words(test_words) == 2
assert count_long_words(test_words, min_length=0) == 7
assert count_long_words(test_words, min_length=4) == 3
assert count_long_words(test_words, min_length=100) == 0

    # Test Driven Development
# При написании сложных функиций можно сначала написать тест-кейсы через assert, а затем реализовывать функцию
# 2. Затем реализуем функцию, чтобы проходила все тесты
def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = dsquared**0.5
    return result

# 1. Сначала прописываем разные известные или граничные случаи
assert distance(1,2, 1,2) == 0
assert distance(3,4, 3,5) == 1
assert distance(3,4, 5,4) == 2
assert distance(1,2, 4,6) == 5
assert distance(0,0, 1,1) == 2**0.5


    # Optional Parameters

# Опциональные параметры — это параметры со значениями по умолчанию.
# Они задаются в определении функции, например:
# def func(x, y=10, z=0): - сначала обязательные, потом опциональные.

# ----------------------------------------------------------
# Важно 1: значения по умолчанию вычисляются ОДИН РАЗ —
# во время определения функции, а не при каждом вызове.
# Пример 1. Значения по умолчанию (y=3, z=initial) запоминаются во время определения функции, а не во время её вызова.
# То есть z=initial означает z=7, потому что initial в тот момент был равен 7.
# Даже если позже ты переопределяешь initial = 10, значение по умолчанию z уже стало 7 и не меняется.
initial = 7
def f(x, y =3, z=initial):
    print("x, y, z, are: " + str(x) + ", " + str(y) + ", " + str(z))

initial = 10
f(2)    # x, y, z, are: 2, 3, 7

# Важно 2: изменяемые значения по умолчанию (например, списки)
# сохраняются между вызовами функции. Это может вызвать баги.
# пример 2: Значение аргумента L=[] создаётся один раз при определении функции, и сохраняется между вызовами.
# Поэтому L в первых трёх вызовах — это один и тот же список, который постепенно накапливает [1, 2, 3].
# В f(4, ["Hello"]) и f(5, ["Hello"]) ты передаёшь новые списки вручную, поэтому там всё ожидаемо.
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))                  # [1]
print(f(2))                  # [1, 2]
print(f(3))                  # [1, 2, 3]
print(f(4, ["Hello"]))       # ['Hello', 4]
print(f(5, ["Hello"]))       # ['Hello', 5]

# как решить
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# Использование именованных аргументов
def introduce(name, age=29, city="Москва"):
    print(f"Имя: {name}, Возраст: {age}, Город: {city}")

introduce("Егор")                           # Имя: Егор, Возраст: 29, Город: Москва
introduce("Егор", 30, "Королев")            # Имя: Егор, Возраст: 30, Город: Королев
introduce("Егор", city="Королев")           # Имя: Егор, Возраст: 29, Город: Королев
introduce("Егор", city="Королев", age=30)   # Имя: Егор, Возраст: 30, Город: Королев
#introduce(city="Королев", age=30", Егор")  # SyntaxError: invalid syntax.


    # Для справки! Ограничения на передачу аргументов 
# Только позиционные параметры (слева от "/")
# Только именованные параметры (справа от "*")
# Между ними — обычные: можно и так, и так
def example(pos1, pos2, /, both, *, kw1, kw2):
    print(f"pos1 = {pos1}, pos2 = {pos2}")
    print(f"both = {both}")
    print(f"kw1 = {kw1}, kw2 = {kw2}")

example(1, 2, both=3, kw1=4, kw2=5)             # Правильно
# example(pos1=1, pos2=2, both=3, kw1=4, kw2=5) # TypeError: pos1 и pos2 должны быть переданы позиционно
# example(1, 2, 3, 4, 5)                        # TypeError: kw1 и kw2 нужно передавать по имени


    # ___ Использование кортежей в функциях и циклах ___ #
    
# Присваивание нескольких значений через кортеж
tup = (13, 46)
atup, btup = tup        # распаковка кортежа (слева и справа кортежи одинаковой длины)
print('atup:', atup, ', \
btup:', btup)          # atup: 13 , btup: 46

alist, blist = [3, 4]   # распаковка оказывается работает и с другими типами данных. лист
print('alist:', alist, ', \
blist:', blist)        # alist: 3 , blist: 4

adict, bdict = {'Name': 'Egor', 'Age': 30}   # словарь
print('adict:', adict, ', \
bdict:', bdict)        # adict: Name , bdict: Age

astr, bstr = 'hi'       # строка
print('astr:', astr, ', \
bstr:', bstr)          # astr: h , bstr: i

# Использование Кортежей в циклах
pokemon = {'Rattata': 19, 'Machop': 66, 'Seel': 86, 'Volbeat': 86, 'Solrock': 126}
p_names = []
p_number = []
for p_nm, p_nb in pokemon.items():
    p_names.append(p_nm)
    p_number.append(p_nb)
print(p_names)    
print(p_number)    

p_names2 = []
for pokemon in pokemon.items():
    p_names2.append(pokemon[0])
print(p_names2)

# Возврат нескольких значений через кортеж
def circleInfo(r):
    """ Return (circumference, area) of a circle of radius r """
    c = 2 * 3.14159 * r
    a = 3.14159 * r * r
    return c, a

print(circleInfo(10))       # (62.8318, 314.159)

circumference, area = circleInfo(1)
print(circumference, area)  # 6.28318 3.14159

# Передача аргументов в функцию в виде кортежа
def add(x, y):
    return x + y

print(add(3, 4))    # 7 
z = (5, 4)
#print(add(z))      # TypeError: add() missing 1 required positional argument: 'y'
print(add(*z))      # 9. * - используется для распаковки кортежей



    # ___ Цикл While ___ #
    
# Цикл While используют:
# - Если не известно число итераций заранее.
import random
x = 0
i = 0
while x != 5:
    x = random.randint(0, 9)
    i +=1
    print('iter:', i, ' x:', x)
print('Done')

# - При ожидании ввода или события.
password = ""
while password != "secret":
    password = input("Введите пароль: ")
print("Доступ разрешен")

# В while-loop можно сделать все то же самое, что и в for-loop
eve_nums = []
i = 0
while i < 15:   # Цикл while выполняет блок кода, пока условие истинно (True).
    if i % 2 == 0:
        eve_nums.append(i)
    i += 1
print(eve_nums) # [0, 2, 4, 6, 8, 10, 12, 14]

eve_nums = []
i = 0
for i in range(15):
    if i % 2 == 0:
        eve_nums.append(i)
print(eve_nums) # [0, 2, 4, 6, 8, 10, 12, 14]

# break and continue
list = []
x = 0
while True:         #  while True: - бесконечный цикл
    x += 1
    if x % 3 == 0:
        continue    # continue переводит на следующую итерацию
    if x > 10:
        break       # break прекращает выполнение цикла
    list.append(x)
    
print(list) # [1, 2, 4, 5, 7, 8, 10]

def sublist(list):
    sl = []
    item = 0
    while item < len(list):
        if list[item] == 5:
            break
        sl.append(list[item])
        item += 1
    return sl


print(sublist([1, 2, 3, 4, 5, 6, 7, 8]))
print(sublist([5]))
print(sublist([8, 6, 5]))
print(sublist([1, 6, 2, 3, 9]))



    # Лямбда-функции

# Лямбда — это компактная, безымянная функция, задаётся через ключевое слово lambda.
# Синтаксис:
# lambda arguments: expression
def func(args):
    return value

func = lambda args: value

# Функция, определённая через def
def f(x):
    return x - 1

print(f)                        # <function f at 0x...> — ссылка на функцию f
print(type(f))                  # <class 'function'>
print(f(3))                     # 2 — вызов функции f

# Анонимная (лямбда) функция:
print(lambda x: x - 1)          # <function <lambda> at 0x...> — тоже функция
print(type(lambda x: x - 1))    # <class 'function'>
print((lambda x: x - 1)(3))     # 2 — вызов лямбда-функции

# Лямбда-функция, сохранённая в переменной
func = lambda x: x - 1

print(func)                     # <function <lambda> at 0x...>
print(type(func))               # <class 'function'>
print(func(3))                  # 2

# Оба способа создают объект типа <function>
# Оба работают одинаково при вызове
# def → для создания именованных, многострочных функций
# Лямбда-функция не имеет имени и предназначена для простых, анонимных выражений (например, в map, filter, sorted)
# Лямбда-функцию присваивают переменной, если нужно компактно описать простую операцию.



    # Обёрточные функции и декораторы: пример с защитой по паролю

# Декоратор: принимает функцию и возвращает обёрнутую версию
def passwordProtect(func):
    def wrappedFunc():
        password = input("Enter the password to call the function: ")

        if password == "password123":
            func()  # вызываем исходную функцию
        else:
            print("Access denied. Sorry")

    return wrappedFunc

# Вариант без синтаксиса @
def printMessage():
    print("Секретное сообщение")

protectedPrint = passwordProtect(printMessage)  # Оборачиваем вручную
protectedPrint()

# Вариант с использованием @decorator 
@passwordProtect    # это означает, что следующая функция будет обернута в passwordProtect
def printMessage2():
    print("Это вторая защищённая функция")

printMessage2()     # при вызове printMessage2() на самом деле вызывается passwordProtect(printMessage2)



    # ___ Функция sorted() и метод .sort() в Python ___

# sorted() — встроенная функция
# работает с любыми итерируемыми объектами (список, строка, кортеж и т.д.)
# возвращает новый отсортированный объект
# не меняет оригинальный

nums = [3, 1, 4, 2]
sorted_nums = sorted(nums)
print(sorted_nums)  # [1, 2, 3, 4]
print(sorted(nums)) # [1, 2, 3, 4]
print(nums)         # [3, 1, 4, 2] — не изменился

# .sort() — метод списка
# работает только со списками
# сортирует **на месте** (in-place)
# ничего не возвращает (возвращает None)

nums.sort()
print(nums)         # [1, 2, 3, 4]
print(nums.sort())  # None

# Оба способа поддерживают опциональные парамтры:
# - reverse=True — сортировка по убыванию
# - key= — функция, по которой сравниваются элементы

# Пример с reverse=True 
words = ['apple', 'banana', 'kiwi', 'lemon', 'pear', 'pineapple']
print(sorted(words, reverse=True))  # ['pineapple', 'pear', 'lemon', 'kiwi', 'banana', 'apple']
words.sort(reverse=True)
print(words)                        # ['pineapple', 'pear', 'lemon', 'kiwi', 'banana', 'apple']

# Пример с key=
# В key мы передаём функцию (или lambda), в которую будет подставляться каждый элемент объекта 
# и сравниваться при сортировке будут уже возвращаемые величины
sorted_by_len = sorted(words, key=len)
print(sorted_by_len)                # ['pear', 'kiwi', 'lemon', 'apple', 'banana', 'pineapple']

# Сортировка по нескольким критериям:
# Что делает lambda x: (-len(x), x):
# - сначала сортирует по длине слова len(x) по убыванию (минус перед len)
# - если длины слов одинаковые, сортирует по алфавиту (второй элемент кортежа)
sorted_by_len = sorted(words, key=lambda x: (-len(x), x)) 
print(sorted_by_len)                # ['pineapple', 'banana', 'apple', 'lemon', 'kiwi', 'pear']


    # ___ Сортировка словарей в Python (Sorting a Dictionary) ___

# Словари (dict) в Python по умолчанию не упорядочены по значению ключей,
# но их можно отсортировать по ключам или значениям.

# Сортировка словаря = сортировка списка кортежей (key, value) через data.items() и sorted()

data = {'apple': 5, 'banana': 2, 'pear': 8, 'grape': 3}

# Сортировка по ключам (по алфавиту)
sorted_by_keys = dict(sorted(data.items())) # dict() обратно превращает список кортежей в словарь
print(sorted_by_keys)       # {'apple': 5, 'banana': 2, 'grape': 3, 'pear': 8}

# Сортировка по значениям (по возрастанию)
sorted_by_values = dict(sorted(data.items(), key=lambda x: x[1]))
print(sorted_by_values)     # {'banana': 2, 'grape': 3, 'apple': 5, 'pear': 8}

# Сортировка по нескольким критериям:
# 1) по значению (по убыванию)
# 2) по ключу (по алфавиту)
data2 = {'apple': 5, 'banana': 2, 'pear': 8, 'grape': 3}

sorted_multi = dict(sorted(data2.items(), key=lambda x: (-x[1], x[0])))
print(sorted_multi)
# {'apple': 5, 'banana': 5, 'pear': 5, 'grape': 3}

# Если нужно получить отсортированный список ключей/значений:
print(sorted(data.keys()))     # ['apple', 'banana', 'grape', 'pear']
print(sorted(data.values()))  # [2, 3, 5, 8]

# Пример
dictionary = {"Flowers": 10, 'Trees': 6, 'Chairs': 6, "Firepit": 1, 'Grill': 2, 'Lights': 22}
# по ключам
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[0]))
sorted_dict = dict(sorted(dictionary.items())) # то же самое
print(sorted_dict)  # {'Chairs': 6, 'Firepit': 1, 'Flowers': 10, 'Grill': 2, 'Lights': 22, 'Trees': 6}
# по значениям
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))
print(sorted_dict)  # {'Firepit': 1, 'Grill': 2, 'Trees': 6, 'Chairs': 6, 'Flowers': 10, 'Lights': 22}
# сначала по значениям, потом по ключам
sorted_dict = dict(sorted(dictionary.items(), key=lambda x: (x[1], x[0])))
print(sorted_dict)  # {'Firepit': 1, 'Grill': 2, 'Chairs': 6, 'Trees': 6, 'Flowers': 10, 'Lights': 22}

# список ключей по алфавиту
sorted_keys = sorted(dictionary.keys())
print(sorted_keys)          # ['Chairs', 'Firepit', 'Flowers', 'Grill', 'Lights', 'Trees']
# список значений по возрастанию
sorted_values = sorted(dictionary.values())
print(sorted_values)        # [1, 2, 6, 6, 10, 22]
# список ключей по возрастанию значений. 
# по умолчанию сортировка идет по ключам, т.е. вместо х подставляются ключи, dictionary[x] - значения
sorted_keys_by_value = sorted(dictionary, key=lambda x: dictionary[x])
print(sorted_keys_by_value) # ['Firepit', 'Grill', 'Trees', 'Chairs', 'Flowers', 'Lights']