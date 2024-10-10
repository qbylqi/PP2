import re

def match_string(input_string):
    pattern = r'a.*b$'  # 'a' за которой следует что угодно и строка заканчивается на 'b'
    return re.match(pattern, input_string)

# Примеры использования
print(match_string("a random string b"))    # Совпадение
print(match_string("ab"))                    # Совпадение
print(match_string("ac"))                    # Нет совпадения
