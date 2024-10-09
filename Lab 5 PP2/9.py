import re

def insert_spaces_before_capitals(s):
    return re.sub(r'([A-Z])', r' \1', s).strip()

# Пример
print(insert_spaces_before_capitals("InsertSpacesHere"))  # 'Insert Spaces Here'
