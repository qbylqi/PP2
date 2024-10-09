import re

def split_at_uppercase(s):
    return re.split(r'(?=[A-Z])', s)

# Пример
print(split_at_uppercase("SplitAtUppercaseLetters"))  # ['Split', 'At', 'Uppercase', 'Letters']
