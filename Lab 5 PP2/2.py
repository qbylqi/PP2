import re

def match_ab_two_to_three(s):
    return bool(re.match(r'ab{2,3}$', s))

# Пример
print(match_ab_two_to_three("abb"))  # True
print(match_ab_two_to_three("abbbb"))  # False
