import os  # Импортируем модуль os

# Определяем функцию для проверки существования пути и извлечения имени файла и директории
def check_path(path):
    if os.path.exists(path):  # Проверяем, существует ли путь
        print("Path exists")
        print("Directory:", os.path.dirname(path))  # Извлекаем часть пути, которая является директорией
        print("Filename:", os.path.basename(path))  # Извлекаем имя файла
    else:
        print("Path does not exist")

# Пример использования
path = "example.txt"
check_path(path)
