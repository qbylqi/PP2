class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Пример использования
rectangle = Rectangle(4, 5)
print(rectangle.area())  # Вывод: 20
"""
Объяснение:
Rectangle: наследует от Shape и переопределяет метод area чтобы вычислять площадь прямоугольника.
"""