# Определяем функцию для проверки на палиндром
def is_palindrome(s):
    return s == s[::-1]  # Сравниваем строку с её обратной версией

# Пример
s = "madam"
result = is_palindrome(s)
print(result)  # Выводим результат
