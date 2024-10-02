def even_numbers(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield str(i)

# Ввод значения n с консоли
n = int(input("Введите число n: "))

# Печать чётных чисел через запятую
print(",".join(even_numbers(n)))
