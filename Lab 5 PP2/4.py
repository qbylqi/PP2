import re

def find_sequences(input_string):
    pattern = r'[A-Z][a-z]+'  # Одна заглавная буква, за которой следуют строчные буквы
    return re.findall(pattern, input_string)

# Примеры использования
print(find_sequences("HelloWorld"))           # ['H', 'W']
print(find_sequences("Python Is Awesome"))    # ['P', 'I', 'A']
