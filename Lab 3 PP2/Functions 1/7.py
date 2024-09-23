def has_33(nums):
    for i in range(len(nums) - 1):
        if nums[i] == 3 and nums[i + 1] == 3:
            return True
    return False

# Пример использования
print(has_33([1, 3, 3]))  # Вывод: True
print(has_33([1, 3, 1, 3]))  # Вывод: False
"""
Объяснение: функция проверяет, есть ли две "3" рядом друг с другом в списке.
"""