import re

def split_string(input_string):
    pattern = r'(?=[A-Z])'  # Перед каждой заглавной буквой
    return re.split(pattern, input_string)

# Примеры использования
print(split_string("HelloWorld"))            # ['H', 'ello', 'W', 'orld']
print(split_string("SplitMeNow"))             # ['S', 'plit', 'M', 'e', 'N', 'ow']
