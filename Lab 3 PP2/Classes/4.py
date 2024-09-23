import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point({self.x}, {self.y})")

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

# Пример использования
p1 = Point(0, 0)
p2 = Point(3, 4)
p1.show()  # Вывод: Point(0, 0)
p2.show()  # Вывод: Point(3, 4)
print(p1.dist(p2))  # Вывод: 5.0
"""
Объяснение:
Класс Point содержит методы для отображения координат, их изменения и вычисления
расстояния между двумя точками.
"""