import re

def match_a_followed_by_anything_ending_in_b(s):
    return bool(re.match(r'a.*b$', s))

# Пример
print(match_a_followed_by_anything_ending_in_b("aXb"))  # True
print(match_a_followed_by_anything_ending_in_b("aX"))  # False
