import re

def snake_to_camel(s):
    return re.sub(r'(_\w)', lambda x: x.group(1)[1].upper(), s)

# Пример
print(snake_to_camel("snake_case_string"))  # 'snakeCaseString'
