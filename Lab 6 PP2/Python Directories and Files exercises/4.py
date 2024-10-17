# Определяем функцию для подсчета строк в файле
def count_lines(filename):
    with open(filename, 'r') as file:  # Открываем файл в режиме чтения
        lines = file.readlines()  # Читаем все строки файла
        return len(lines)  # Возвращаем количество строк

# Пример использования
filename = "example.txt"
line_count = count_lines(filename)
print(f"Number of lines: {line_count}")
