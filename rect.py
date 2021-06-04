class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def increase_height(self, amount):
        self.height += amount

    def perimeter(self):
        return (self.width + self.height) * 2

    def info(self):
        return "Площадь:{}\nПериметр:{}".format(
            self.area(),
            self.perimeter()
        )

    def __str__(self):
        return "Прямоугольник(w={},h={})\n(S={},P={})".format(
            self.width,
            self.height,
            self.area(),
            self.perimeter()
        )

    def __add__(self, other):
        return Rectangle(
            self.width + other.width,
            self.height + other.height
        )
