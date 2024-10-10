import re

def replace_characters(input_string):
    pattern = r'[ ,.]'  # Пробел, запятая или точка
    return re.sub(pattern, ':', input_string)

# Примеры использования
print(replace_characters("Hello, world. How are you?"))  # 'Hello:world:How:are:you?'
