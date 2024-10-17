import os  # Импортируем модуль os

# Определяем функцию для удаления файла
def delete_file(path):
    if os.path.exists(path):  # Проверяем, существует ли файл
        if os.access(path, os.W_OK):  # Проверяем, доступен ли для записи (значит, можем удалить)
            os.remove(path)  # Удаляем файл
            print(f"File {path} deleted")
        else:
            print(f"File {path} is not writable")
    else:
        print(f"File {path} does not exist")

# Пример использования
delete_file('example.txt')
