# Определяем функцию, которая принимает кортеж
def all_true(tup):
    return all(tup)  # Используем встроенную функцию all, которая возвращает True, если все элементы кортежа истинные

# Пример
tup = (True, True, False)
result = all_true(tup)
print(result)  # Выводим результат
