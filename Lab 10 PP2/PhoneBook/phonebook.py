import csv
import chardet

# Функция для загрузки данных из CSV
def load_data_from_csv(file_path):
    # Определение кодировки файла
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        print(f"Определенная кодировка: {result['encoding']}")

    # Открытие файла с найденной кодировкой
    with open(file_path, mode='r', encoding=result['encoding'], newline='') as file:
        reader = csv.reader(file)
        data = []
        for row in reader:
            # Проверяем, что строка не пустая и содержит хотя бы два элемента
            if len(row) >= 2:
                data.append(row)
            else:
                print(f"Пропущена некорректная строка: {row}")
        return data

# Функция для добавления записи вручную
def add_manual_entry():
    first_name = input("Введите имя пользователя: ")
    phone = input("Введите номер телефона: ")
    return [first_name, phone]

# Функция для отображения всех данных
def display_data(data):
    print("\nТелефонная книга:")
    for entry in data:
        print(f"Имя: {entry[0]}, Телефон: {entry[1]}")

# Главная программа
def main():
    print("1. Загрузить данные из CSV")
    print("2. Добавить запись вручную")
    
    choice = input("Выберите действие (1 или 2): ")
    
    if choice == '1':
        file_path = input("Введите путь к файлу CSV: ")
        try:
            data = load_data_from_csv(file_path)
            display_data(data)
        except Exception as e:
            print(f"Ошибка при загрузке данных из CSV: {e}")
    
    elif choice == '2':
        data = []
        entry = add_manual_entry()
        data.append(entry)
        display_data(data)
    
    else:
        print("Неверный выбор, попробуйте снова.")

# Запуск программы
if __name__ == "__main__":
    main()
