import re

def camel_to_snake(s):
    return re.sub(r'([A-Z])', r'_\1', s).lower()

# Пример
print(camel_to_snake("camelCaseString"))  # 'camel_case_string'
