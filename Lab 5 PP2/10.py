import re

def camel_to_snake(camel_str):
    pattern = r'(?<!^)(?=[A-Z])'  # Находим место перед каждой заглавной буквой, кроме первой
    return re.sub(pattern, '_', camel_str).lower()

# Примеры использования
print(camel_to_snake("HelloWorld"))            # 'hello_world'
print(camel_to_snake("ThisIsATest"))           # 'this_is_a_test'
