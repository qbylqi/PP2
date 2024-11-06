# Импортируем библиотеки pygame, random и time, которые понадобятся для работы с графикой, случайными числами и временем
import pygame
import random, time

# Инициализируем pygame, чтобы начать использовать его функции
pygame.init()

# Устанавливаем переменную, которая будет контролировать главный игровой цикл
running = True

# Устанавливаем ширину и высоту окна
WIDTH, HEIGHT = 1200, 800

# Устанавливаем FPS (кадры в секунду) для контроля скорости обновления игры
FPS = 60

# Определяем цвета, которые будем использовать: красный, черный и синий
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Устанавливаем начальный уровень игры
LEVEL = 0

# Создаем шрифт Verdana размером 20 для вывода текста на экран
font = pygame.font.SysFont("Verdana", 20)

# Создаем текст "Game Over" для отображения в конце игры
game_over = font.render("Game Over", True, BLACK)

# Создаем игровое окно заданного размера
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Устанавливаем название окна "Anaconda"
pygame.display.set_caption("Anaconda")

# Создаем объект clock для контроля скорости игры
clock = pygame.time.Clock()

# Функция для обработки событий
def handler():
    # Проходим по всем событиям
    for event in pygame.event.get():
        # Если событие "Выход", то возвращаем False, чтобы выйти из цикла
        if event.type == pygame.QUIT:
            return False
    # Если нет события выхода, возвращаем True
    return True

# Функция для проверки столкновений змеи со стенками
def check_collision(x, y):
    global running
    # Если координаты головы змеи выходят за границы экрана
    if x >= WIDTH or x < 0 or y >= HEIGHT or y < 40:
        # Задержка на полсекунды перед отображением "Game Over"
        time.sleep(0.5)
        # Заливаем экран красным цветом
        screen.fill(RED)
        # Выводим текст "Game Over" в центре экрана
        screen.blit(game_over, (550, 400))
        # Выводим набранные очки
        scoretag = font.render("Your score: " + str(s.score), True, BLACK)
        screen.blit(scoretag, (550, 500))
        
        # Обновляем экран для отображения изменений
        pygame.display.update()
        
        # Задержка на 2 секунды перед завершением игры
        time.sleep(2)
        
        # Завершаем работу pygame
        pygame.quit()

# Класс Snake описывает поведение и свойства змеи
class Snake(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Начальные координаты головы змеи
        self.x = 600
        self.y = 400
        # Начальная скорость змеи
        self.dx = 3
        self.dy = 3
        # Начальный счет
        self.score = 0
        # Увеличение скорости при достижении новых уровней
        self.i = 5
        # Начальное направление движения
        self.direction = "RIGHT"
        # Ограничения на движение змеи, чтобы она не могла двигаться в противоположную сторону
        self.directionsnake = {"LEFT": False, "RIGHT": True, "UP": True, "DOWN": True}
        # Создаем прямоугольник для головы змеи
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
        # Создаем список сегментов змеи (начиная с одного сегмента)
        self.segments = [(self.x, self.y)]
    
    # Обработка нажатий клавиш для управления змеей
    def press(self):
        # Получаем состояния всех клавиш
        pressed_keys = pygame.key.get_pressed()
        # Словарь, связывающий клавиши со значениями направления
        directions = {pygame.K_LEFT: 'LEFT', pygame.K_RIGHT: 'RIGHT', pygame.K_UP: 'UP', pygame.K_DOWN: 'DOWN'}
        # Проверяем, какая клавиша нажата, и обновляем направление
        for key, direction in directions.items():
            if pressed_keys[key]:
                if direction == "LEFT" and self.directionsnake["LEFT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": True, "RIGHT": False, "UP": True, "DOWN": True}
                elif direction == "RIGHT" and self.directionsnake["RIGHT"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": False, "RIGHT": True, "UP": True, "DOWN": True}
                elif direction == "UP" and self.directionsnake["UP"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": True, "RIGHT": True, "UP": True, "DOWN": False}
                elif direction == "DOWN" and self.directionsnake["DOWN"]:
                    self.direction = direction
                    self.directionsnake = {"LEFT": True, "RIGHT": True, "UP": False, "DOWN": True}

    # Метод для перемещения змеи
    def move(self):
        global LEVEL
        # Получаем координаты головы змеи
        head_x, head_y = self.segments[0]
        # Изменяем координаты головы в зависимости от направления
        if self.direction == 'LEFT':
            head_x -= self.dx
        elif self.direction == 'RIGHT':
            head_x += self.dx
        elif self.direction == 'UP':
            head_y -= self.dy
        elif self.direction == 'DOWN':
            head_y += self.dy
        # Обновляем прямоугольник для головы змеи
        self.rect = pygame.Rect(head_x, head_y, 10, 10)
        # Добавляем новый сегмент в начало списка сегментов
        self.segments.insert(0, (head_x, head_y))
        
        # Проверяем, съела ли змея фрукт
        if not pygame.sprite.spritecollide(self, fruits, False):
            # Если не съела, удаляем последний сегмент (змея не растет)
            self.segments.pop()
        else:
            # Если съела, увеличиваем счет
            self.score += 1
            # Если счет кратен i, увеличиваем уровень и скорость
            if s.score % self.i == 0:
                s.dx += 0.4
                s.dy += 0.4
                self.i += 10
                LEVEL += 1

    # Отрисовка змеи
    def draw(self):
        # Рисуем каждый сегмент змеи в красном цвете
        for segment in self.segments:
            pygame.draw.rect(screen, RED, (segment[0], segment[1], 10, 10))

# Класс Fruits описывает поведение и свойства фрукта
class Fruits(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Устанавливаем случайные координаты для фрукта
        self.x = random.randrange(10, 1190, 50)
        self.y = random.randrange(40, 790, 50)
        # Создаем прямоугольник для фрукта
        self.rect = pygame.Rect(self.x, self.y, 10, 10)
    
    # Метод для рисования фрукта
    def born(self):
        # Рисуем фрукт синим цветом
        pygame.draw.rect(screen, BLUE, self.rect)

# Создаем экземпляр змеи и фрукта
s = Snake()
f = Fruits()

# Создаем группу спрайтов для фруктов и добавляем в нее фрукт
fruits = pygame.sprite.Group()
fruits.add(f)

# Основной цикл игры
while running:
    # Ограничиваем FPS до значения, заданного в переменной FPS
    clock.tick(FPS)
    # Обрабатываем события
    running = handler()
    # Заполняем экран черным цветом
    screen.fill(BLACK)
    # Рисуем линию сверху для отображения области счёта и уровня
    pygame.draw.aaline(screen, BLUE, [0, 40], [1200, 40])
    
    # Создаем текст с текущим счетом
    scoretag = font.render("Score: " + str(s.score), True, (0, 255, 0))
    # Создаем текст с текущим уровнем
    leveltag = font.render("Level: " + str(LEVEL), True, (0, 255, 0))
    # Отображаем текст на экране
    screen.blit(scoretag, (10, 10))
    screen.blit(leveltag, (1100, 10))
    
    # Рисуем каждый фрукт в группе
    for entity in fruits:
        entity.born()

    # Обрабатываем нажатия клавиш для управления змеей
    s.press()
    # Перемещаем змею
    s.move()

    # Проверяем столкновение змеи с фруктом и создаем новый фрукт, если есть столкновение
    if pygame.sprite.spritecollide(s, fruits, True):
        f = Fruits()
        fruits.add(f)

    # Рисуем змею
    s.draw()
    
    # Проверяем столкновение змеи с краями экрана
    check_collision(s.segments[0][0], s.segments[0][1])

    # Обновляем экран для отображения всех изменений
    pygame.display.update()

# Завершаем работу pygame
pygame.quit()
