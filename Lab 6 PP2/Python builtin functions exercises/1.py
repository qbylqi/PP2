import math  # Импортируем модуль math для использования функции prod

# Определяем функцию, которая принимает список чисел
def multiply_list(lst):
    return math.prod(lst)  # Используем встроенную функцию prod, которая перемножает все элементы списка

# Пример
numbers = [1, 2, 3, 4]
result = multiply_list(numbers)
print(result)  # Выводим результат
