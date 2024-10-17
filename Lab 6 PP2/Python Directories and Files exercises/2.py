import os  # Импортируем модуль os

# Определяем функцию для проверки доступа
def check_access(path):
    print("Existence:", os.path.exists(path))  # Проверяем, существует ли путь
    print("Readable:", os.access(path, os.R_OK))  # Проверяем, доступен ли для чтения
    print("Writable:", os.access(path, os.W_OK))  # Проверяем, доступен ли для записи
    print("Executable:", os.access(path, os.X_OK))  # Проверяем, является ли исполняемым

# Пример использования
path = "example.txt"
check_access(path)
