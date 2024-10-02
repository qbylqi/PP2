def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

# Пример использования
a = int(input("Введите начальное число a: "))
b = int(input("Введите конечное число b: "))

for square in squares(a, b):
    print(square)
