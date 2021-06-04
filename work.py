import beth
from math import sqrt


def safe_rectangle_area(a, b):
    try:
        return beth.rectangle_area(a, b)
    except ArithmeticError:
        return "Ошибка"

