import re

def find_sequences(input_string):
    pattern = r'[a-z]+(_[a-z]+)+'  # Последовательности строчных букв с подчеркиванием
    return re.findall(pattern, input_string)

# Примеры использования
print(find_sequences("hello_world"))         # ['hello_world']
print(find_sequences("this_is_a_test"))      # ['this_is_a_test']
print(find_sequences("no_underscores"))      # []
