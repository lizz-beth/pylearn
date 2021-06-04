# Типы данных и переменные
# int (целые числа), str (строки), bool (логические)

# коллекции:
#   список a.k.a. list — [1,2,3,'a',3] — упорядочен, может иметь дубликаты
#   изменяемый

#   множество a.k.a. set {1,2,3} - не упорядочено, не имеет дубликатов
#   изменяемое

#   кортеж a.k.a tuple (1,2,3,'a','b') - как список, но неизменяемый

#   frozen set — как множество, только не изменяемое

# обращение с коллекцией (прямое обращение к элементам и взятие подколлекций):
#   прямое обращение по индексу (доступно только для упорядоченных структур)
#       letters = ['a', 'b', 'c']
#       letters[0] -> 'a', letters[2] -> 'c', letters[3] -> 'error'
#       также обратиться можно с "конца":
#       letters[-1] -> 'c', letters[-2] -> ['b']
#   срезы — взятие части коллекции от нижней границы (вкл.) до верхней (не вкл.)
#       letters[0:2] -> ['a', 'b'], letters[0:3] -> ['a', 'b', 'c']
#   ** advanced
#   срез с шагом — взятие части коллекции с определенным шагом
#       digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#       digits[::2] -> [0,2,4,6,8,10]
#       digits[::3] -> [0,3,6,9]
#       digits[::-1] -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (обратный порядок)
#   **
#   пробежка по коллекции (итерирование по коллекции, циклы)
#       for <variable_name> in <collection_name>:
#           ...do some stuff with <variable_name>
#       letters = ['a', 'b', 'c', 'd', 'e', 'f']
#
#       for letter in letters:
#           print("letter is " + letter)

# Функции
# def <имя функции>(имена аргументов):
#     ...


# range(a,b) -> [a,b) (от а до b не включая верхнюю границу)
# range(1, 10) -> [1,2,3...,9]
# range(10) -> [0,1,2,3...,9]
# for — "пробежка по массиву"
#
# square = lambda x: x * x
# concate = lambda s1, s2: s1 + s2
# compose = lambda f, g: lambda x: f(g(x))

def age_category(years):
    if years < 0:
        raise Exception("Age cannot be negative")
    if years > 50:
        return "senior"
    elif years > 20:
        return "average"
    else:
        return "young"


def sum(col):
    s = 0
    for elem in col:
        s += elem
    return s


def count(col):
    s = 0
    for elem in col:
        print("add {} to sum {}".format(1, s))
        s += 1
    return s


#
# print(count([1, 2, 3, 4]))


def amount(elements):
    s = 0
    for elem in elements:
        print("adding {} to {}".format(elem, s))
        s += elem
    return s


#
#
def sum_info(elements):
    if not elements:
        raise Exception("collection cannot be empty")
    return "final sum for {} is {}".format(elements, amount(elements))


#
#
# nums = []
# print(sum_info(elements=nums))

def invite(title_plural, *names):
    formatted_names = ", ".join(names)
    print("Дорогие {}, а именно: {}".format(title_plural, formatted_names))


def roots_of_quadratic(a, b, c):
    import math
    d = discriminant(a, b, c)
    if d < 0:
        raise ArithmeticError("root are not real (negative discriminant)")
    first_root = (-b + math.sqrt(d)) / (2 * a)
    if d == 0:
        return [first_root]
    elif d > 0:
        second_root = (-b - math.sqrt(d)) / (2 * a)
        return [first_root, second_root]


def discriminant(a, b, c):
    return b ** 2 - 4 * a * c


def info(msg, f, *args):
    return "{} {}".format(msg, f(*args))


# print(info("total sum is", sum, [1, 2, 3]))

#
# file = open("files/weather.txt", "w")
# file.write("hello")
# file.close()

def logging(func):
    def new_func(*args):
        print(
            "executing '{}' for args {}".format(
                func.__name__,
                args
            )
        )
        return func(*args)

    return new_func


@logging
def sum(a, b):
    return a + b


# print(sum(3, 4))

def replace_first_arg(arg_value):
    def wrapper(func):
        def new_func(*args):
            return func(arg_value, *args[1:])

        return new_func

    return wrapper


@replace_first_arg(10)
def mult(a, b):
    return a * b


def timed(func):
    import time

    def new_func(*args):
        before = time.time()
        result = func(*args)
        print("execution time is {} s".format(time.time() - before))
        return result

    return new_func


def no_return(func):
    def new_func(*args):
        res = func(*args)
        return "{}-symbol return was blocked".format(
            len(res)
        )

    return new_func


@no_return
@timed
def mapped(collection, func):
    return [func(i) for i in collection]


# print(
#     mapped(
#         range(100_000_000),
#         lambda x: x * x
#     )
# )
