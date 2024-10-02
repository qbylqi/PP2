import math

def polygon_area(num_sides, side_length):
    return (num_sides * side_length ** 2) / (4 * math.tan(math.pi / num_sides))

# Пример использования
num_sides = 4
side_length = 25
area = polygon_area(num_sides, side_length)
print(f"Input number of sides: {num_sides}\nInput the length of a side: {side_length}\nThe area of the polygon is: {area:.1f}")
