import os  # Импортируем модуль os для работы с файловой системой

# Определяем функцию для вывода директорий и файлов
def list_dir_files(path):
    print("Directories:")  # Выводим сообщение для директорий
    for item in os.listdir(path):  # Проходим по каждому элементу в указанной директории
        if os.path.isdir(os.path.join(path, item)):  # Проверяем, является ли элемент директорией
            print(item)  # Выводим название директории

    print("\nFiles:")  # Выводим сообщение для файлов
    for item in os.listdir(path):  # Проходим по элементам в указанной директории
        if os.path.isfile(os.path.join(path, item)):  # Проверяем, является ли элемент файлом
            print(item)  # Выводим название файла

    print("\nAll Directories and Files:")  # Выводим все элементы
    for item in os.listdir(path):  # Проходим по всем элементам в директории
        print(item)  # Выводим имя каждого элемента

# Пример использования
path = "."  # Текущая директория
list_dir_files(path)
