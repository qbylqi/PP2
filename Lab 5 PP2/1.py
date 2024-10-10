import re

def match_string(input_string):
    pattern = r'a(b*)'  # 'a' за которой следуют ноль или более 'b'
    return re.match(pattern, input_string)

# Примеры использования
print(match_string("a"))           # Совпадение: 'a'
print(match_string("ab"))          # Совпадение: 'ab'
print(match_string("abbbbb"))      # Совпадение: 'abbbbb'
print(match_string("b"))           # Нет совпадения
