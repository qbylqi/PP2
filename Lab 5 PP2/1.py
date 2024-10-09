import re

def match_ab_zero_or_more(s):
    return bool(re.match(r'a*b*$', s))

# Пример
print(match_ab_zero_or_more("a"))  # True
print(match_ab_zero_or_more("abbbb"))  # True
print(match_ab_zero_or_more("b"))  # False
