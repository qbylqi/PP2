import re

def match_string(input_string):
    pattern = r'ab{2,3}'  # 'a' за которой следуют 2 или 3 'b'
    return re.match(pattern, input_string)

# Примеры использования
print(match_string("abb"))          # Совпадение: 'abb'
print(match_string("abbb"))         # Совпадение: 'abbb'
print(match_string("a"))            # Нет совпадения
print(match_string("abbbb"))        # Нет совпадения
