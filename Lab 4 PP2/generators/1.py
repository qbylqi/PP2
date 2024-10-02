def generate_squares(N):
    for i in range(N):
        yield i ** 2

# Пример использования
for square in generate_squares(5):
    print(square)
