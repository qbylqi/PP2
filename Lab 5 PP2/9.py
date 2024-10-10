import re

def insert_spaces(input_string):
    pattern = r'(?=[A-Z])'  # Перед каждой заглавной буквой
    return ' '.join(re.split(pattern, input_string))

# Примеры использования
print(insert_spaces("HelloWorld"))              # 'Hello World'
print(insert_spaces("ThisIsATest"))             # 'This Is A Test'
