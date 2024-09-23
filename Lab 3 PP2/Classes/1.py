class InputOutputString:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Введите строку: ")

    def printString(self):
        print(self.s.upper())

# Пример использования
obj = InputOutputString()
obj.getString()
obj.printString()
"""
Объяснение:
Класс InputOutputString Содержит два метода:
getString: Для получения строки из консоли.
printString: для вывода строки в верхнем регистре.
"""