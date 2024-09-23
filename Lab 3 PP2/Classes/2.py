class Shape:
    def __init__(self):
        pass

    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length

    def area(self):
        return self.length ** 2

# Пример использования
square = Square(4)
print(square.area())  # Вывод: 16
"""
Объяснение:
Shape: базовый класс, где метод area по умолчанию возвращает 0.
Square: подкласс, который наследует Shapе и переопределяет метод area чтобы вычислять площадь квадрата.
"""