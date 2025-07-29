# _____ Python Classes and Inheritance _____


    # Classes 

# Термины

# Класс — пользовательский составной тип (шаблон), в котором описано, какие переменные (атрибуты) и функции (методы) будут у объектов. 
# Объект (экземпляр класса) — конкретный экземпляр класса, созданный по его шаблону. У объекта есть своё состояние (значения переменных) и поведение (методы).
# Поле (атрибут) — переменная, хранящаяся внутри объекта. Атрибуты определяют состояние объекта и задаются в __init__.
# Метод — функция, определённая внутри класса. Методы описывают, что умеет делать объект, и вызываются через экземпляр (например, obj.method()).
# Переменная экземпляра — переменная, связанная с конкретным объектом (self.variable). У каждого объекта она может иметь своё значение.
# Переменная класса — переменная, общая для всех объектов класса. Определяется внутри класса вне методов. Обращение: ClassName.variable.
# Метод экземпляра — обычный метод, первым аргументом которого идёт self. Позволяет работать с переменными конкретного объекта.
# Метод класса — метод, первым аргументом которого идёт cls. Определяется с декоратором @classmethod и работает с переменными самого класса.
# Статический метод — метод без доступа к self или cls. Используется, когда логика метода не зависит от состояния объекта или класса. Объявляется через @staticmethod.
# Сигнатура функции — это её имя + список параметров с их порядком и типами (если указаны).
# Параметры — переменные, указанные в сигнатуре функции или метода. Получают значения из аргументов при вызове.
# Аргументы — конкретные значения, переданные при вызове функции или метода, чтобы соответствовать параметрам.
# Публичные переменные — переменные, которые можно свободно читать и изменять снаружи класса. В Python все переменные по умолчанию публичные.
# Приватные переменные — переменные, начинающиеся с двойного подчёркивания __. Они защищены от прямого доступа извне через механизм name mangling (self.__x становится self._ClassName__x).



# Основы
class Car:
    pass        # pass - заглушка, когда синтаксис требует, чтобы что-то было, но ты ещё не реализовал поведение.

my_car = Car()  # создание объекта (экземпляра класса) с помощью конструктора (специального метода)


# Поля: переменные экземпляра и класса
class Car:
    wheels = 4                  # переменная класса (общая для всех машин)

    def __init__(self, color):  # cоздание инициализатора, метода, который вызывается при инициализации объекта в качестве конструктора
        self.color = color      # переменная экземпляра (уникальна для каждой машины)

car1 = Car("red")
car2 = Car("blue")

print(car1.color)   # red
print(car2.color)   # blue
print(car1.wheels)  # 4


# Методы: экземпляра, класса и статический
class Car:
    total_cars = 0

    def __init__(self, color):
        self.color = color
        Car.total_cars += 1

    def honk(self):  # метод экземпляра
        print("Beep beep!")

    @classmethod
    def show_total(cls):  # метод класса
        print(f"Total cars: {cls.total_cars}")

    @staticmethod
    def info():  # статический метод
        print("Cars are means of transportation")

car = Car("green")
car.honk()           # Beep beep!
Car.show_total()     # Total cars: 1
Car.info()           # Cars are means of transportation


# Аргументы и параметры 
def greet(name):  # name — параметр
    print("Hello,", name)

greet("Egor")  # "Egor" — аргумент


# Публичные и приватные переменные
class User:
    def __init__(self, name, password):
        self.name = name               # публичная
        self.__password = password     # приватная

    def get_password(self):
        return self.__password

u = User("Egor", "12345")
print(u.name)             # OK
#print(u.__password)    # Ошибка (AttributeError)
print(u.get_password())   # OK


# Специальные методы (магические методы)
# Эти методы начинаются и заканчиваются двойным подчёркиванием (__method__).
# Используются для настройки поведения объектов класса.

class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Person: {self.name}"

    def __len__(self):
        return len(self.name)
    
    def __call__(self):
        print(f"Hello, I'm {self.name}")

p1 = Person("Egor")
p2 = Person("Egor")
print(str(p1))      # Person: Egor
print(len(p1))      # 4
p1()                # Hello, I'm Egor

# Часто используемые специальные методы:
# - __init__(self, ...)     — инициализация объекта
# - __str__(self)           — строковое представление (print)
# - __eq__(self, other)     — оператор ==
# - __lt__(self, other)     — определяет поведение оператора <  def __lt__(self, other):    # less than
#                                                                   return self.price < other.price
# - __len__(self)           — функция len()
# - __call__(self)          — позволяет вызывать объект как функцию


# Приватные элементы в Python 

class Example:
    def __init__(self):
        self.public = "Я общедоступен"
        self._protected = "Я защищённый (protected), по соглашению"
        self.__private = "Я приватный (private) с name mangling" # __var переименовывается в _ClassName__var

    def get_private(self):
        return self.__private

e = Example()

print(e.public)             # Доступно везде
print(e._protected)         # Технически доступно, но по соглашению не трогать
# print(e.__private)        # Ошибка! Атрибут не найден

# Обход name mangling:
print(e._Example__private)  # Получаем приватное значение



# Примеры с учебы

import math

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    count = 0               # переменная класса

    def __init__(self, initX, initY):

        self.x = initX      # переменная экземпляра
        self.y = initY
        Point.count += 1    # на переменную класса ссылаюсь через Point

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def distance(self, point2):                 # метод, считает расстояние от конкретного экземпляра до точки
        xdiff = point2.getX()-self.getX()
        ydiff = point2.getY()-self.getY()
        
        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist
    
    def distancePoints1(point1, point2):        # функция класса, считает расстояние от между двумя точками
        xdiff = point2.getX()-point1.getX()
        ydiff = point2.getY()-point1.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist
    
    @staticmethod                               # чтобы можно было вызывать через экземпляр. пример ниже
    def distancePoints2(point1, point2):         
        xdiff = point2.getX()-point1.getX()
        ydiff = point2.getY()-point1.getY()

        dist = math.sqrt(xdiff**2 + ydiff**2)
        return dist
    
    def __str__(self):                  # специальный метод
        return "x = {}, y = {}".format(self.x, self.y)
    
    def halfway(self, target):
        mx = (self.x + target.x)/2
        my = (self.y + target.y)/2
        return Point(mx, my)            # Возвращает точку

p = Point(4,3)
q = Point(0,0)

print(p.distanceFromOrigin())
print(p.distance(q))

#print(q.distancePoints1(p,q))      # TypeError, Python автоматически передаёт экземпляр p как первый аргумент. @staticmethod - решает эту проблему.
print(q.distancePoints2(p,q))   
print(Point.distancePoints1(p,q))   # Лучше так вызывать 
print(Point.distancePoints2(p,q))   #               методы класса (функции класса)


class Cereal:
    def __init__(self, str1, str2, int1):
        self.name = str1
        self.brand = str2
        self.fiber = int1
    
    def __str__(self):
        return f'{self.name} cereal is produced by {self.brand} and has {self.fiber} grams of fiber in every serving!'
        
c1 = Cereal('Corn Flakes', "Kellogg's", 2)   
c2 = Cereal('Honey Nut Cheerios', "General Mills", 3) 

print(c1)
print(c2)


# dir() – просмотр атрибутов и методов
# dir(Cereal) — показывает все атрибуты и методы класса (включая магические)
"""
[
 '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__'
]
"""
# dir(c1) — показывает всё то же самое плюс переменные экземпляра
"""
[
 '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',
 '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__',
 '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__',
 '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__',
 '__subclasshook__', '__weakref__',
 'brand', 'fiber', 'name'
]
"""


# Тестирование классов

#testing class constructor (__init__ method)
p = Point(3, 4)
assert p.y == 4
assert p.x == 3

#testing the distance method
p = Point(3, 4)
assert p.distanceFromOrigin() == 5.0



    # Наследование классов

# Наследование — это механизм, с помощью которого один класс (называется подкласс, subclass) 
# может наследовать свойства и поведение другого класса (называемого суперкласс, superclass или base class).

# superclass
class Animal:           
    count = 0           # переменная класса

    def __init__(self, name):
        self.name = name
        Animal.count += 1

    def sleep(self):    # метод
        print("Zzz")

    def speak(self):    # метод
        print("Some sound")

# subclass
class Dog(Animal):      # В скобках пишем родительский класс
    def speak(self):    # Переопределение метода
        print("Woof!")

a = Animal("a")
dog = Dog("b")

print(Animal.count)     # 2 Dog тоже посчитался
print(dog.name)         # b - вызвался инизиализатор родительского класса
dog.speak()             # Woof!


# subclass
class Cat(Animal):      

    def __init__(self, name, breed):    # Создание своего инициализирующего метода
        super().__init__(name)          # с помощью ключевого слова super сслыаемся на родительский метод
        self.breed = breed              # добавляем свою переменную

    def speak(self):    # Переопределение метода
        print("Meow!")

cat = Cat("c", "siam")

print(Animal.count)     # 3
cat.speak()             # Some sound
print(cat.breed)        # siam


# Множественное наследование в Python
# Python позволяет создавать класс, который наследует поведение от двух и более базовых классов.
# Однако лучше избегать множественного наследования, если только оно не даёт реального преимущества и не делает код чище и понятнее.

class BreedClass(Cat, Dog):
    pass

# Если оба родительских класса имеют метод с одинаковым именем, Python выбирает из первого родительского класса
class Mother:
    eyes = "Brown"
    def hello(self):
        print("Привет от Мамы")

class Father:
    eyes = "Blue"
    def hello(self):
        print("Привет от Папы")

class Child(Mother, Father):  # порядок важен!
    pass

Ivan = Child()
print(Ivan.eyes)    # Brown
Ivan.hello()        # Привет от Мамы


# Полиморфизм в Python
# Полиморфизм - это способность объектов разных классов использовать один и тот же интерфейс (одинаковые имена методов), 
# но при этом реализовывать поведение по-своему.

# animal_sound работает с любым объектом, у которого есть метод speak() — неважно, какой это класс. Это и есть полиморфизм.
def animal_sound(animal):
    animal.speak()

animal_sound(dog)  # Woof!
animal_sound(cat)  # Meow!


# Как интерпретатор ищет атрибуты:
# 1. Проверяет в экземпляре класса. 
# 2. Если не найдено, ищет в с самом классе
# 3. Проверяет родительский класс
# 4. Проверяет следующих предков по порядку до конца.


    # Декораторы

# Повтор. Декоратор функции
def addLogging(func):           # Это декоратор — он принимает функцию в качестве аргумента.
    def wrapper(x):             # Это обёртка (wrapper-функция), которая заменит оригинальный метод.
                                # Она должна принимать те же аргументы, что и оригинальный метод.
                                # В случае метода — первый аргумент всегда self, а далее — любые аргументы (здесь x — один аргумент)
        print(f"Before")        # Первый лог
        result = func(x)        # Это вызов оригинального метода, который был передан как func. Ему передаются все нужные аргументы.
        print(f"After")         # Второй лог
        return result           # Возвращается результат, который вернул оригинальный метод.
    return wrapper              # Возвращается обёртка, которая содержит в себе логи и результат выполнения функции.
                                # Теперь обёртка будет использоваться вместо оригинальной функции.

@addLogging
def printName(name):
    print(f"My name is {name}")

printName("Egor")       # Before
                        # My name is Egor
                        # After


# Декоратор метода: логирование вызовов. Универсальный
def universal_logger(func):
    def wrapper(*args, **kwargs):               # *args и **kwargs делают декоратор универсальных на любое количество аргументов
        print(f"Calling: {func.__name__}")
        print(f"  args: {args}")
        print(f"  kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

# Применение к обычной функции
@universal_logger
def add(a, b):
    return a + b

add(3, 5)           # Calling: add
                    #   args: (3, 5)
                    #   kwargs: {}
                    # Result: 8

# Применение к методу класса
class Calculator:
    @universal_logger
    def multiply(self, x, y):
        return x * y

calc = Calculator()
calc.multiply(4, 6) # Calling: multiply
                    #   args: (<__main__.Calculator object at 0x...>, 4, 6)
                    #   kwargs: {}
                    # Result: 24


# Декоратор класса: добавление метода
def addBeep(cls):
    def beep(self):
        print(f"{self.model} says 'Beep!'")
    cls.beep = beep
    return cls

@addBeep
class Car:
    def __init__(self, make, model, color, mileage):
        self.make = make
        self.model = model
        self.color = color
        self.mileage = mileage

mustang = Car("Ford", "Mustang", "blue", 0)
mustang.beep()      # Mustang says 'Beep!'


# Декораторы с аргументами
def repeat(n):
    """Декоратор, который повторяет выполнение функции n раз"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi!")

say_hi()  # напечатает "Hi!" три раза


# Модуль functools
# Предоставляет утилиты для работы с функциями и декораторами, особенно когда функции нужно модифицировать, оборачивать или кэшировать.

# Самое полезное: @functools.wraps
# Когда ты создаёшь свой декоратор, Python заменяет оригинальную функцию обёрткой (wrapper). В результате теряется имя, докстрока, аннотации и т.д.
# Чтобы сохранить оригинальные свойства функции — используют @functools.wraps.

import functools
import time

def performance(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()     # "Start" timer
        result = func(*args, **kwargs)
        end_time = time.perf_counter()       # "Stop" timer
        elapsed_time = end_time - start_time 
        return result, elapsed_time
    return wrapper

@performance
def say_hello():
    """Prints a greeting"""
    print("Hello!")

say_hello()                 # Hello!
                            # (None, 4.700000863522291e-05) - None, потому что обертка возвращает (result, elapsed_time)
print(say_hello.__name__)   # say_hello
print(say_hello.__doc__)    # Prints a greeting



# Динамические аргументы позволяют передать любое количество аргументов в функцию без заранее известного количества параметров.

# Динамические позиционные аргументы: *args
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3))           # 6
print(sum_all(5, 10, 15, 20))     # 50

# Динамические именованные аргументы: **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Egor", age=30, city="Korolyov")

# Комбинирование *args и **kwargs
# def example(pos1, *args, kw1=None, **kwargs):


    # Exceptions Исключения

# Исключения — это ошибки, которые возникают во время выполнения программы.

#Базовая структура обработки исключений

try:
    print (1/0)
except :
    print("Произошла ошибка")   # Произошла ошибка
finally:                                # не обязательная часть
    print("Этот код выполнится всегда") # Даже если ошибки нет, finally будет выполнен

#   Есть встроенные типы исключений:
# ZeroDivisionError — деление на ноль
# ValueError — неправильное значение
# TypeError — несоответствие типов
# IndexError — выход за границы списка
# KeyError — отсутствует ключ в словаре
# FileNotFoundError — файл не найден
# AttributeError — обращение к несуществующему атрибуту
# и много других

# Пример:
try:
    x = int(input("Введите число: "))
    print(10 / x)
except ZeroDivisionError:
    print("Нельзя делить на ноль!")
except ValueError:
    print("Это не число!")


# Создание собственных исключений
class NegativeNumberError(ValueError):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Отрицательное число не допускается: {value}")

def square_root(x):
    if x < 0:
        raise NegativeNumberError(x)    # Ключевое слово raise используется, чтобы намеренно вызвать исключение — встроенное или пользовательское.
    return x ** 0.5

try:
    print(square_root(-25))
except NegativeNumberError as e:
    print(e)  # Отрицательное число не допускается: -25