def solve(numheads, numlegs):
    for rabbits in range(numheads + 1):
        chickens = numheads - rabbits
        if rabbits * 4 + chickens * 2 == numlegs:
            return chickens, rabbits
    return None, None

# Пример использования
chickens, rabbits = solve(35, 94)
print(f"Кур: {chickens}, Кроликов: {rabbits}")  # Вывод: Кур: 23, Кроликов: 12
"""
Объяснение: функция перебирает все возможные комбинации количества кроликов и кур, проверяя условие на количество ног.
"""