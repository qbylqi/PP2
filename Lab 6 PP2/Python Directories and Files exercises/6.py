import string  # Импортируем модуль string для работы с символами

# Определяем функцию для создания текстовых файлов
def create_files():
    for letter in string.ascii_uppercase:  # Проходим по каждой букве от A до Z
        filename = f"{letter}.txt"  # Формируем имя файла
        with open(filename, 'w') as file:  # Открываем файл в режиме записи
            file.write(f"This is file {filename}")  # Записываем текст в файл

# Пример использования
create_files()
