import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

# Примеры использования
print(snake_to_camel("hello_world"))  # 'helloWorld'
print(snake_to_camel("snake_case_example"))  # 'snakeCaseExample'
