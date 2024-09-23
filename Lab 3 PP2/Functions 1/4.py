def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]

# Пример использования
print(filter_prime([2, 3, 4, 5, 6, 7, 8, 9, 10]))  # Вывод: [2, 3, 5, 7]
"""
Объяснение: filter_prime возвращает список только из простых чисел, используя вспомогательную функцию is_prime
"""