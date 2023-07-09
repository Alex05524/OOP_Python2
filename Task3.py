class Archive:
    """
    Класс Archive хранит пару свойств: число и строку.
    Старые данные сохраняются в списковых архивах.
    """

    number_archive = []
    string_archive = []

    def __init__(self, number, string):
        """
        Инициализация объекта Archive.

        Аргументы:
        - number: Число.
        - string: Строка.
        """
        self.number = number
        self.string = string
        self.number_archive.append(number)
        self.string_archive.append(string)

    def get_number_archive(self):
        """
        Возвращает список чисел из архива.
        """
        return self.number_archive

    def get_string_archive(self):
        """
        Возвращает список строк из архива.
        """
        return self.string_archive

    def __repr__(self):
        """
        Возвращает представление объекта Archive для программиста.
        """
        return f"Archive(number={self.number}, string='{self.string}')"

    def __str__(self):
        """
        Возвращает представление объекта Archive для пользователя.
        """
        return f"Число: {self.number}, Строка: {self.string}"

# Пример использования
archive1 = Archive(42, "Hello")
print(repr(archive1))  # Выводит представление объекта Archive для программиста
print(archive1)  # Выводит представление объекта Archive для пользователя

archive2 = Archive(123, "World")
print(repr(archive2))  # Выводит представление объекта Archive для программиста
print(archive2)  # Выводит представление объекта Archive для пользователя

print(archive1.get_number_archive())  # Выводит список чисел из архива
print(archive1.get_string_archive())  # Выводит список строк из архива