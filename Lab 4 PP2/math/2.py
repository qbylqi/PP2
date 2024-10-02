def trapezoid_area(height, base1, base2):
    return (base1 + base2) * height / 2

# Пример использования
height = 5
base1 = 5
base2 = 6
area = trapezoid_area(height, base1, base2)
print(f"Height: {height}\nBase, first value: {base1}\nBase, second value: {base2}\nExpected Output: {area}")
