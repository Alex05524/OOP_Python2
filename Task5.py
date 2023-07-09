class Rectangle:
    """
    Класс Rectangle представляет прямоугольник.
    """

    def __init__(self, length, width=None):
        """
        Инициализация объекта Rectangle.

        Аргументы:
        - length: Длина прямоугольника.
        - width: Ширина прямоугольника. Если не указана, считается, что у нас квадрат.
        """
        self.length = length
        self.width = width if width is not None else length

    def get_perimeter(self):
        """
        Возвращает периметр прямоугольника.
        """
        return 2 * (self.length + self.width)

    def get_area(self):
        """
        Возвращает площадь прямоугольника.
        """
        return self.length * self.width

    def __add__(self, other):
        """
        Перегрузка оператора сложения для прямоугольников.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает новый прямоугольник суммарного периметра.
        """
        total_perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle(total_perimeter // 4)

    def __sub__(self, other):
        """
        Перегрузка оператора вычитания для прямоугольников.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает новый прямоугольник с разницей периметров. Если разница меньше нуля, создается квадрат.
        """
        difference = self.get_perimeter() - other.get_perimeter()
        if difference < 0:
            return Rectangle(0)
        else:
            return Rectangle(difference // 4)

    def __lt__(self, other):
        """
        Перегрузка оператора < для сравнения прямоугольников по площади.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает True, если текущий прямоугольник имеет меньшую площадь.
        """
        return self.get_area() < other.get_area()

    def __le__(self, other):
        """
        Перегрузка оператора <= для сравнения прямоугольников по площади.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает True, если текущий прямоугольник имеет меньшую или равную площадь.
        """
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        """
        Перегрузка оператора > для сравнения прямоугольников по площади.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает True, если текущий прямоугольник имеет большую площадь.
        """
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        """
        Перегрузка оператора >= для сравнения прямоугольников по площади.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает True, если текущий прямоугольник имеет большую или равную площадь.
        """
        return self.get_area() >= other.get_area()

    def __eq__(self, other):
        """
        Перегрузка оператора == для сравнения прямоугольников по площади.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает True, если площади прямоугольников равны.
        """
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        """
        Перегрузка оператора != для сравнения прямоугольников по площади.

        Аргументы:
        - other: Другой прямоугольник.

        Возвращает True, если площади прямоугольников не равны.
        """
        return self.get_area() != other.get_area()

    def __str__(self):
        """
        Возвращает строковое представление объекта Rectangle.
        """
        return f"Прямоугольник: Длина={self.length}, Ширина={self.width}"

# Пример использования
rectangle1 = Rectangle(5, 3)
print(rectangle1)  # Выводит строковое представление объекта Rectangle
print("Периметр:", rectangle1.get_perimeter())  # Выводит периметр прямоугольника
print("Площадь:", rectangle1.get_area())  # Выводит площадь прямоугольника

rectangle2 = Rectangle(4)
print(rectangle2)  # Выводит строковое представление объекта Rectangle
print("Периметр:", rectangle2.get_perimeter())  # Выводит периметр прямоугольника

# Примеры сравнения прямоугольников по площади
print(rectangle1 < rectangle2)  # Выводит True, если площадь rectangle1 меньше площади rectangle2
print(rectangle1 <= rectangle2)  # Выводит True, если площадь rectangle1 меньше или равна площади rectangle2
print(rectangle1 > rectangle2)  # Выводит True, если площадь rectangle1 больше площади rectangle2
print(rectangle1 >= rectangle2)  # Выводит True, если площадь rectangle1 больше или равна площади rectangle2
print(rectangle1 == rectangle2)  # Выводит True, если площади прСравнение прямоугольников по площади было добавлено в предыдущий пример. Пожалуйста, обратите внимание на методы `__lt__`, `__le__`, `__gt__`, `__ge__`, `__eq__` и `__ne__`, которые обеспечивают сравнение прямоугольников по площади. Вы можете использовать эти методы для выполнения всех шести операций сравнения (`<`, `<=`, `>`, `>=`, `==`, `!=`) между прямоугольниками.

rectangle1 = Rectangle(5, 3)
rectangle2 = Rectangle(4)

print(rectangle1 < rectangle2)  # True
print(rectangle1 <= rectangle2)  # True
print(rectangle1 > rectangle2)  # False
print(rectangle1 >= rectangle2)  # False
print(rectangle1 == rectangle2)  # False
print(rectangle1 != rectangle2)  # True