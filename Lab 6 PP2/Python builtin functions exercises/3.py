# Определяем функцию для проверки на палиндром
s = input()
def is_palindrome(s):
    return s == s[::-1]  # Сравниваем строку с её обратной версией
    
# Выводим результат
result = is_palindrome(s)
print(result)  
