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
print("Площадь:", rectangle2.get_area())  # Выводит площадь прямоугольника

rectangle3 = rectangle1 + rectangle2
print(rectangle3)  # Выводит строковое представление объекта Rectangle после сложения
print("Периметр:", rectangle3.get_perimeter())  # Выводит периметр прямоугольника после сложения

rectangle4 = rectangle3 - rectangle2
print(rectangle4)  # Выводит строковое представление объекта Rectangle после вычитания
print("Периметр:", rectangle4.get_perimeter())  # Выводит периметр прямоугольника после вычитания