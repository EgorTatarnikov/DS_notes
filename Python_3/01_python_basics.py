#_____ Python Basics _____#

# создаем простейшие функции
def square(x):
    return x * x

def sub (x, y):
    return x - y

def exchange (x, y):
    temp = x
    x = y
    y = temp
    return x, y

print(sub(5, 1))

print(sub(5, sub(4, 1)))


# 150 строк разбираемся с типами данных, изменяемостью и хранением в памяти
t1 = (5, 1)
t2 = 4, 2

print(type(t2))         # <class 'tuple'>

print(exchange(1, 5))   # (5, 1)

x1, x2 = exchange(1, 5)     # это называется распаковка кортежа (tuple unpacking)
                            # Python сразу «распаковывает» его — присваивает первое значение переменной x1, 
                            #                                                       второе — переменной x2.
x1, x2                      # (5, 1)
print(x1, x2)               # 5 1
print(type(exchange(1, 5))) # <class 'tuple'>

print(square(5))            #

print(type("Hello World!"))

print('''Hello          
How are you?''')            # ''' ''' и """ """ позволяет писать многостроковые строки

print('Hello \\ ')          # \ позволяет написать после него зарещенные символы
print('hi\'')

print(45000)        # 45000
print(45_000)       # 45000
print(45, 000)      # 45 0

print(45, "hello", x1)      # 45 hello 5
#print(45 + "hello") #error
print(str(45) + "hello")    # 45hello

type('c')           # <class 'str'> В Python нет отдельного типа для отдельных символов
print(ord('a'))     # ord() в Python возвращает числовой код (Unicode) символа.

in1 = input('Input smth: ')
print('Type of in1:', type(in1))

n = input("Please enter your name: ")
print("Hello", n)

my_age = int(input('How old I am: '))
print('My age:', my_age, '\nType of "my_age":', type(my_age))
print(int(1.9)) # output 1

i = int()
print(i)
i = 'hi'
print(i)        # иллюстрация динамического типизирования.

a = 'hello'

# Python при запуске создаёт заранее объекты int для чисел от –5 до 256 и повторно использует их, 
# чтобы ускорить работу и сэкономить память.
a = 100
b = 100
print(id(a))    # 140717307187080
print(id(b))    # 140717307187080
print(a == b)   # True 
print(a is b)   # True — оба указывают на один и тот же объект
x = 1000
y = 1000
print(id(x))    # 2648153138224
print(id(y))    # 2648153141872 отличается
print(x == y)   # True
print(x is y)   # False — это разные объекты, хотя значения равны


print(id(a))    # 2648156418480
b = a
print(id(b))    # 2648156418480 также
print(a == b)   # True
a = 500
print(id(a))    # 2648153141456 поменялось
print(b)        
print(id(b))    # 2648156418480 осталось без изменения
print(a == b)   # False
# int и str неизменяемые. 
# В Python переменные — это ссылки на объекты, а не "ячейки памяти", как в C.
# Присваивание b = a копирует ссылку, но не сам объект.
# При переназначении a (перенаправлении её на другой объект), b остаётся привязанной к старому.

a = 7
b = 8
print(hex(id(a)))   # 0x7ffb4d1bc3e8
print(hex(id(b)))   # 0x7ffb4d1bc408
b = 8 - 1
print(hex(id(a)))   # 0x7ffb4d1bc3e8
print(hex(id(b)))   # 0x7ffb4d1bc3e8
print(a == b)       # True
print(a is b)       # True


# Листы изменяемые
l1 = [1, 2, 3]
l2 = l1
print(hex(id(l1)))  # 0x268926c1bc0
print(hex(id(l2)))  # 0x268926c1bc0
l1.append(4)
print(l1)           # [1, 2, 3, 4]
print(l2)           # [1, 2, 3, 4]
print(hex(id(l1)))  # 0x268926c1bc0 адрес не поменялся
print(hex(id(l2)))  # 0x268926c1bc0
print(l1 == l2)     # True — значения одинаковые
print(l1 is l2)     # True — это один и тот же объект

l1 = [4, 5, 6]      # не изменил а переназначил.
print(hex(id(l1)))  # 0x2689266ef00 новый адрес
print(hex(id(l2)))  # 0x268926c1bc0 старый адрес
print(l1 == l2)     # False - значения разные
print(l2 is l2)     # False - объекты разные

l1 = [1, 2, 3, 4]   # переназначил старые значения
print(l1)           # [1, 2, 3, 4]
print(l2)           # [1, 2, 3, 4]
print(hex(id(l1)))  # 0x268926c1680 новый адрес
print(hex(id(l2)))  # 0x268926c1bc0 не совпадает
print(l1 == l2)     # True — значения одинаковые
print(l1 is l2)     # False - объекты разные

print(len('hello'))

x = 0
x += 3  # increment x by 3; same as x = x + 3
print(x)
x += 1
print(x)


l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(hex(id(l1)))  # 0x268926c1680
print(hex(id(l2)))  # 0x2689266ef00
print(l1 == l2)     # True — значения одинаковые
print(l1 is l2)     # False - объекты разные


from my_module import calculate
calculate(4, 4)

import random
print(random.random())
print(random.randrange(1, 10))

a = 502
b = 503
print(id(a))    # 2648153138224
print(id(b))    # 2648153140944

3/2     # 1.5 деление всегда дает в результате флоат
3/3     # 1.0
1+1.0   # 2.0
x = 10
x **= 3 
print(x)    # 1000
x = 0b11    # бинарная запись чисел
x = 0o74    # восьмиричная
x = 0xa13   # шестнадцатиричная
print(x)    # 2579, при выводе переводит в десятичную

print(bin(15)) # 0b1111
print(oct(15)) # 0o17
print(hex(15)) # 0xf

x = 3e310   # максимальное значение для float ограничено — обычно это около 1.8e308
print(x)    # inf
type(x)     # float


# Decimal
from decimal import Decimal

d = Decimal(10)
print(d/20)
print(0.1 + 0.2)
print(Decimal(0.1)+Decimal(0.2)) #неточно

a = Decimal("0.1")  # Важно: всегда создавай Decimal из строк, 
b = Decimal("0.2")  # чтобы избежать неточностей при преобразовании float.
print(type(a))


# Tuples, Lists and Strings
print(a + b)
x = 1, 2
y = (2,)
print(type(x))
print(x)
print(y)
empty_tuple = ()
empty_tuple = tuple()


# Indexes
str = "Hello World!"
print(str[-1])
for char in str:
    print(char)


# The Slice Operator
print(str[3:5])
h = str[:5] # элемент с индексом 5 не включается
w = str[6:]
print(h, w)

list_1 = ['Tatarnikov', 'Egor', 30, 'Korolev']
print(list_1)
print(list_1[1])
print(list_1[:2])       # ['Tatarnikov', 'Egor']
print(list_1[0][:5])    # Tatar

tuple_1 = ('Tatarnikov', 'Egor', 30, 'Korolev')
print(tuple_1)
print(tuple_1[1])
print(tuple_1[:2])      # ('Tatarnikov', 'Egor')
print(tuple_1[0][:5])   # Tatar

# Python автоматически интернирует некоторые строки, особенно: короткие строки (например, 'a', 'abc')
# Интернирует — значит хранит в одном экземпляре и переиспользует один и тот же объект в памяти, 
# вместо создания новых. Это оптимизация памяти и скорости.
str = 'a'
print(id(str))  # 140717306530904
s = 'a'
print(id(s))    # 140717306530904
print(str is s) # True — интернирование


dict_2 = {'Family Name': 'Tatarnikov',
          'First Name': 'Egor',
          'Age': 30,
          'City': 'Korolev'}
print(dict_2)
print(dict_2['Age'])

dict_3 = {
    'Family Name': ['Tatarnikov', 'Basova'],
    'First Name': ['Egor', 'Svetlana'],
    'Age': [30, 28],
    'City': ['Korolev', 'Korolev']
}
for key in dict_3.keys():
    print(key)
for value in dict_3.values():
    print(value)
dict_3['Age'][0]

str = 'Hello World!'
str.count('l')  # количество вхождений
str.index('l')  # индекс первого вхождения
str.index('lo') # первого символа первого вхождения

str = 'Hello World!'
l1 = str.split()
print(l1)
print(type(l1))
l2 = str.split('o') # можно назначить сепаратор
print(l2)

s = ' '             # назначаем строку склеиватель
s.join(l1)

'o'.join(l2)        # !!!

alist = [1, 3, 5]
print(alist + alist)
print(alist * 3)
alist.count(5)  # количество вхождений
alist.index(5)  # индекс первого вхождения



# The for Loop
for i in range(5):
    print(i)
    #i += 1     # не нужна, i сама берет следуюшее значение из range на каждом шаге
    i += 2      # вывод все равно 0 1 2 3 4
    
for i in range(0, 10, 2):   # дмапазон от 0 (включительно) до 10 (не включая) с шагом 2
    print(i)    # 0 2 4 6 8
    
for num in [1, 3, 42, 21]:
    print(num)
    
for num in (1, 3, 42, 21):
    print(num)
    
for char in "Hello":
    print(char)

dict_2 = {'Family Name': 'Tatarnikov',
          'First Name': 'Egor',
          'Age': 30,
          'City': 'Korolev'}

for k in dict_2:
    print(k)    # Family Name ... печатает ключи
    
fruits = ['apple', 'pear', 'apricot', 'cherry', 'peach']

for fruit in fruits:
    print(fruit)  
    
for i in range(len(fruits)):    # we can iterate through the indexes by generating a sequence of them, using the range function
    print(i, fruits[i])         # 0 apple ...
    
    
# Turtle class    
import turtle
egor = turtle.Turtle()
egor.forward(100)


# if conditions
x = int(input("Enter x: "))
if x < 5:
    print('x < 5')
else:
    print('x >= 5')
    
if x < 5:
    print('x < 5')
elif x < 10:
    print('5 <= x < 10')   
else:
    print('x >= 10')


# Boolean Expressions
print(True)
print(type(True))
print(type(False))
print(type(bool('True')))
x = 1
y = 2
x == y               # x is equal to y
x != y               # x is not equal to y
x > y                # x is greater than y
x < y                # x is less than y
x >= y               # x is greater than or equal to y
x <= y               # x is less than or equal to y


# Logical operators: and, or, not
x = True
y = False
print(x and y)
print(x or y)
print(not x)

if x and (x or y):
    x = not x
    print('x:', x)
else:
    x = not y
    y = not y
    print('y:', y)


# in, not in
print('a' in 'a')           # True
print('apple' in 'apple')   # True
print('' in 'a')            # True
print('' in 'apple')        # True

print('x' not in 'apple')   # True

print("a" in ["a", "b", "c", "d"])  # True
print(2.0 in [3, 2, 9, 10, 9.0])    # True

y = ["0", 2]
z = [0, 1]
# is x inside of y or z
'x' in y or z # wrong
'x' in y or 'x' in z


# assert - Оператор assert  полезен при отладке программ, поскольку позволяет быстро обнаружить проблемы
# assert останавливает программу, если условие ложно, с выбросом исключения AssertionError
def divider(x, y):
    assert y != 0, 'Деление на ноль'
    print(x / y)
    return x / y

# divider(5, 0)   # AssertionError: Деление на ноль

"""
If the code has conditional blocks (if..elif..else) 
then you’ll want to have tests that check that the right block executes when you expect it to.
"""
x = 3
y = 4
if x < y:
    z = x
else:
    if x > y:
        z = y
    else:
        ## x must be equal to y
        assert x==y
        z = 0
      
      
        
# Sequence Mutation

fruit = ["banana", "apple", "cherry"]
print(hex(id(fruit)))   # 0x22f38371f40
fruit[0] = "pear"
print(hex(id(fruit)))   # 0x22f38371f40 не изменилось

alist = ['a', 'b', 'c', 'd', 'e', 'f']
alist[1:3] = []  # Удаляются элементы с индексами 1 и 2: 'b' и 'c'
print(alist)     # ['a', 'd', 'e', 'f']

alist[4:4] = ['e']  # Вставка 'e' перед элементом с индексом 4 (то есть перед 'f')
print(alist)        # ['a', 'd', 'e', 'e', 'f']

a = ['one', 'two', 'three']
del a[1]  # Удаляется элемент с индексом 1: 'two'
print(a)  # ['one', 'three']

a.remove('three')  # Удаляется элемент со значением 'three'
print(a)           # ['one']

# копирование (клонирование) листов
import copy

a = [1, 2, [3, 4]]
b = a                  # ссылка — всё общее
c = a.copy()           # поверхностная копия — вложенные объекты общие
d = a[:]               # тоже поверхностная копия
e = copy.deepcopy(a)   # глубокая копия — всё независимое

# Меняем исходный список:
a[0] = 'x'
a[2][0] = 'y'

print("a =", a)  # ['x', 2, ['y', 4]]
print("b =", b)  # ['x', 2, ['y', 4]] — то же самое, потому что ссылка
print("c =", c)  # [1, 2, ['y', 4]] — верхний уровень скопирован, вложенный остался общим
print("d =", d)  # [1, 2, ['y', 4]] — как и c
print("e =", e)  # [1, 2, [3, 4]] — полностью независимая копия




# Methods on Strings and Lists

# Examples of working with list methods in Python

# append(item) – adds a single item to the end of the list (modifies the list in place)
lst = [1, 2, 3]
lst.append(4)
print(lst)  # [1, 2, 3, 4]

# Using the concatenation operator "+" creates a new list (new object)
lst = [1, 2, 3]
print(hex(id(lst)))  # 0x7f8b582c5c00 — original list
lst = lst + [4]
print(lst)  # [1, 2, 3, 4]
print(hex(id(lst)))  # 0x7f8b582c5d00 — new object created

# Using += (in-place addition) modifies the existing list without changing its identity
lst = [1, 2, 3]
print(hex(id(lst)))  # 0x7f8b582c5e00 — original list
lst += [4]
print(lst)  # [1, 2, 3, 4]
print(hex(id(lst)))  # 0x7f8b582c5e00 same as before — list modified in place

# Summary:
# - append() → in-place, adds one element
# - +        → creates new list object (new id)
# - +=       → in-place, adds elements from another iterable (like extend)


# insert(position, item) – вставляет элемент на указанную позицию
lst.insert(1, 99)  # [1, 99, 2, 3, 4]

# pop() – удаляет и возвращает последний элемент списка
last = lst.pop()  # last = 4, lst = [1, 99, 2, 3]

# pop(position) – удаляет и возвращает элемент по индексу
second = lst.pop(1)  # second = 99, lst = [1, 2, 3]

# sort() – сортирует список по возрастанию (изменяет сам список)
lst.sort()  # [1, 2, 3]

# reverse() – разворачивает список в обратном порядке (изменяет сам список)
lst.reverse()  # [3, 2, 1]

# index(item) – возвращает индекс первого вхождения элемента
idx = lst.index(2)  # idx = 1

# count(item) – возвращает количество вхождений элемента
ct = lst.count(3)  # ct = 1

# remove(item) – удаляет первое вхождение элемента
lst.remove(3)  # lst = [2, 1]




# Examples of working with string methods in Python

s = "  Hello, World! Hello!  "

# upper() – возвращает строку в верхнем регистре
print(s.upper())  # "  HELLO, WORLD! HELLO!  "

# lower() – возвращает строку в нижнем регистре
print(s.lower())  # "  hello, world! hello!  "

# strip([chars]) – удаляет пробелы или любые символы из переданной строки с начала и конца исходной строки
print(s.strip())  # "Hello, World! Hello!"
print(s.strip(" !,H"))  # "ello, World! Hello"

# count(sub[, start[, end]]) – возвращает количество неперекрывающихся вхождений подстроки
print(s.count("Hello"))  # 2
print(s.count("l"))      # 5

# index(sub[, start[, end]]) – возвращает индекс первого вхождения или вызывает ValueError, если не найдено
print(s.index("World"))  # 10
# print(s.index("Python"))  # ValueError, если раскомментировать

# replace(old, new[, count]) – заменяет все (или некоторые) вхождения подстроки
s2 = s.replace("World", "Python")  
print(s2)  # "  Hello, Python! Hello!  "

# замена с указанием количества (только первые две "l")
s3 = s.replace("l", "*", 2)
print(s3)  # "  He**o, World! Hello!  "

# split([sep]) – разбивает строку по пробелам (или указанному разделителю) в список
words = s.split()  # ['Hello,', 'World!', 'Hello!']
print(words)

# split с кастомным разделителем
csv = "apple,banana,grape"
print(csv.split(","))  # ['apple', 'banana', 'grape']

# join(iterable) – объединяет элементы последовательности, вставляя между ними строку-разделитель
joined = "-".join(["2025", "06", "03"])
print(joined)  # "2025-06-03"

# startswith(prefix[, start[, end]]) – проверяет, начинается ли строка с prefix
print(s.startswith("  He"))  # True

# endswith(suffix[, start[, end]]) – проверяет, заканчивается ли строка на suffix
print(s.endswith("!  "))  # True



# Расширенный пример format с именованными аргументами
template2 = "Coordinates: {lat}, {lon}"
print(template2.format(lat="55.7558° N", lon="37.6173° E"))  # "Coordinates: 55.7558° N, 37.6173° E"

# Строки в Python неизменяемы – при изменении создаётся новый объект
print(hex(id(s)))  # адрес в памяти до модификации
s = s.strip()
print(hex(id(s)))  # другой адрес после модификации (новый объект)


# format and f-string

name = "Egor"
last_name = "Tatarnikov"
language = "Python"

# вариант без format и f -строк
print("My name is " + name + " " + last_name + " and I code in " + language + ".")

# format
template = "My name is {} and I code in {}."
formatted = template.format(name + " " + last_name, language)
print(formatted)  # My name is Egor Tatarnikov and I code in Python.
# чаще пишут сразу так
print("My name is {} and I code in {}.".format(name + " " + last_name, language))

# f-string
print(f"My name is {name} {last_name} and I code in {language}.")


mile = 1609.344
print("Mile is {:.2f} kilometers".format(mile)) # ... 1609.34 ...
print(f"Mile is {mile:.2f} kilometers")         # ... 1609.34 ...


# Accumulating Lists and Strings

alist = [4, 2, 8, 6, 5]
blist = []
clist = []

# Добавляем к каждому элементу alist значение 5 и накапливаем в blist
for item in alist:
    blist.append(item + 5)
print(blist)

# Альтернативный способ накопления с использованием индексов
for i in range(len(alist)):
    clist.append(alist[i] + 5)
print(clist)


text = "hello"
new_text_1 = ""
new_text_2 = ""

# Накапливаем символы строки, преобразуя их в верхний регистр
for char in text:
    new_text_1 += char.upper()

print(new_text_1) # HELLO

# Альтернативный способ накопления с использованием индексов
for i in range(len(text)):
    new_text_2 += text[i].upper()

print(new_text_2) # HELLO

# Don’t Mutate A List That You Are Iterating Through
colors = ["Red", "Purple", "Yellow"]

for i in range(len(colors)):    # IndexError: list index out of range
	if colors[i] == "Purple":
	    del colors[i]
	
print(colors)