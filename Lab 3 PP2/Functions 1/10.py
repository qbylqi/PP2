def unique_elements(lst):
    unique_lst = []
    for item in lst:
        if item not in unique_lst:
            unique_lst.append(item)
    return unique_lst

# Пример использования
print(unique_elements([1, 2, 2, 3, 4, 4, 5]))  # Вывод: [1, 2, 3, 4, 5]
"""
Объяснение: функция возвращает список с уникальными элементами, не используя set.
"""