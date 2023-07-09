import time

class MyString:
    """
    Класс MyString расширяет функциональность обычной строки.
    Дополнительно хранит имя автора строки и время создания.
    """

    def __init__(self, value, author):
        """
        Инициализация объекта MyString.

        Аргументы:
        - value: Значение строки.
        - author: Имя автора строки.
        """
        self.value = value
        self.author = author
        self.creation_time = time.time()

    def get_author(self):
        """
        Возвращает имя автора строки.
        """
        return self.author

    def get_creation_time(self):
        """
        Возвращает время создания строки в формате времени.
        """
        return self.creation_time

    def __str__(self):
        """
        Возвращает строковое представление объекта MyString.
        """
        return f"Строка: {self.value}, Автор: {self.author}, Время создания: {self.creation_time}"

# Пример использования
my_str = MyString("Пример строки", "John Doe")
print(my_str)  # Выводит строковое представление объекта MyString
print(my_str.get_author())  # Выводит имя автора строки
print(my_str.get_creation_time())  # Выводит время создания строки