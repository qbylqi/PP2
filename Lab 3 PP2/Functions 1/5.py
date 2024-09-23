from itertools import permutations

def print_permutations(s):
    perms = permutations(s)
    for p in perms:
        print(''.join(p))

# Пример использования
print_permutations('abc')
"""
Объяснение: функция использует библиотеку itertools для создания всех перестановок строки.
"""