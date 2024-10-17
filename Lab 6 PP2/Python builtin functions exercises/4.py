import time  # Импортируем модуль time для работы с временем
import math  # Импортируем модуль math для работы с квадратными корнями

# Определяем функцию, которая принимает число и задержку в миллисекундах
def delayed_sqrt(num, ms):
    time.sleep(ms / 1000)  # Используем time.sleep для задержки в секундах (ms/1000 для перевода миллисекунд в секунды)
    return math.sqrt(num)  # Возвращаем квадратный корень

# Пример
num = 25100
ms = 2123
result = delayed_sqrt(num, ms)
print(f"Square root of {num} after {ms} milliseconds is {result}")  # Выводим результат
