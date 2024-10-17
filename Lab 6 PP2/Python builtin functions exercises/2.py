# Определяем функцию, которая принимает строку
def count_letters(s):
    upper_case = sum(1 for c in s if c.isupper())  # Считаем заглавные буквы
    lower_case = sum(1 for c in s if c.islower())  # Считаем строчные буквы
    return upper_case, lower_case

# Пример
s = "Hello World"
upper, lower = count_letters(s)
print(f"Upper case: {upper}, Lower case: {lower}")  # Выводим результат
