def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Пример использования
print(is_palindrome("madam"))  # Вывод: True
print(is_palindrome("hello"))  # Вывод: False
#Объяснение: функция удаляет пробелы, приводит строку к нижнему регистру и проверяет, совпадает ли строка с её обратной версией.