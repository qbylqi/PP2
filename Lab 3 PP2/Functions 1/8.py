def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# Пример использования
print(spy_game([1, 2, 4, 0, 0, 7, 5]))  # Вывод: True
print(spy_game([1, 7, 2, 0, 4, 5, 0]))  # Вывод: False
"""
Объяснение: функция отслеживает порядок чисел 0, 0 и 7 в списке.
"""