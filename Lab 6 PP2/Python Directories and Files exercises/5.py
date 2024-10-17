# Определяем функцию для записи списка в файл
def write_list_to_file(filename, lst):
    with open(filename, 'w') as file:  # Открываем файл в режиме записи
        for item in lst:  # Проходим по каждому элементу списка
            file.write(f"{item}\n")  # Записываем каждый элемент в файл с новой строки

# Пример использования
my_list = ['apple', 'banana', 'cherry']
write_list_to_file('fruits.txt', my_list)
