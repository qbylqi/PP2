# Определяем функцию для копирования содержимого файла
def copy_file(source, destination):
    with open(source, 'r') as src_file:  # Открываем исходный файл в режиме чтения
        content = src_file.read()  # Читаем содержимое файла
    with open(destination, 'w') as dest_file:  # Открываем целевой файл в режиме записи
        dest_file.write(content)  # Записываем содержимое в целевой файл

# Пример использования
copy_file('example.txt', 'copy_example.txt')
