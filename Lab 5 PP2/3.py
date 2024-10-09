import re

def find_lowercase_with_underscore(s):
    return re.findall(r'[a-z]+_[a-z]+', s)

# Пример
print(find_lowercase_with_underscore("test_case"))  # ['test_case']
