import pygame #для создания игры 
from pygame.locals import * #и упрощенного доступа к константам (например, K_LEFT).
import random, time #для генерации случайных координат, для управления паузами.
import sys #для выхода из программы.


pygame.init() #инициализирует модули Pygame.
running = True #флаг для основного игрового цикла.
WIDTH = 400 #ширина и высота окна игры.
HEIGHT = 600
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255) #Цветовые переменные: BLUE, RED, GREEN, BLACK, WHITE — задают основные цвета в формате RGB.
SPEED = 5 #начальная скорость движения объектов.
FPS = 60 #частота кадров в секунду.
screen = pygame.display.set_mode((WIDTH, HEIGHT)) #Создаем окно screen с заданной шириной и высотой.
pygame.display.set_caption("Racer") #задает название окна игры.
clock = pygame.time.Clock() #объект для управления частотой кадров.
background = pygame.image.load("Racer/Images/animatedstreet.png") #загружает изображение фона.
SCORE = 0
COINS = 0 #начальные значения очков и монет.

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20) #font и font_small — шрифты для отображения текста в игре.
game_over = font.render("Game Over", True, BLACK) #рендерит текст "Game Over" черного цвета для отображения при проигрыше.


def handler(): #Функция handler() обрабатывает события:
    global SPEED
    for event in pygame.event.get():
        if event.type == INC_SPEED: # увеличивает скорость на 0.5 каждые 2 секунды.
            SPEED += 0.5
        if event.type == QUIT: #завершает игру при закрытии окна.
            return False
    return True

class Enemy(pygame.sprite.Sprite):  #Класс Enemy создает врага (препятствие).
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Racer/Images/enemy.png") #загружает изображение врага.
        self.rect = self.image.get_rect() #область, занимаемая изображением.
        self.rect.center = (random.randint(40,WIDTH-40),-10)
    def move(self): #перемещает врага вниз по экрану со скоростью SPEED
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30,WIDTH-40),0)
    def draw(self, surface):
        surface.blit(self.image, self.rect) #Если враг выходит за нижнюю границу, увеличивает SCORE, и перемещает его в случайную точку сверху.

class Coins(pygame.sprite.Sprite):  #Класс Coins создает монету, аналогично Enemy
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Racer/Images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)
    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600): #Если монета выходит за границы, возвращается наверх и меняет координаты.
            self.rect.top = 0
            self.rect.center = (random.randint(30,WIDTH-40),0)
            if pygame.sprite.spritecollideany(self, enemies):
                self.rect.center = (random.randint(30,WIDTH-40),0) #Проверка на столкновение с врагами, чтобы не появляться в одном месте с ними.
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(pygame.sprite.Sprite): #Класс Player создает игрока
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Racer/Images/player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self): #move() перемещает игрока влево или вправо при нажатии клавиш.
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)
    def draw(self, surface):
        surface.blit(self.image, self.rect)

#Создаем объекты игрока, врага и монеты.
P1 = Player()
E1 = Enemy()
C1 = Coins()
enemies = pygame.sprite.Group()
enemies.add(E1)
coins_s = pygame.sprite.Group() #Группы enemies и coins_s — для управления множественными объектами этих типов.
coins_s.add(C1)
all_sprites = pygame.sprite.Group() # группа для всех спрайтов, чтобы отрисовывать и перемещать их в цикле.
all_sprites.add(P1)
all_sprites.add(E1)


INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 2000) #пользовательское событие, увеличивающее скорость каждые 2 секунды.

while running:
    clock.tick(FPS) #Ограничиваем частоту кадров с помощью clock.tick(FPS).
    running = handler() #Вызываем handler() для обработки событий.

    screen.blit(background, (0,0)) #Рисуем фон.
    scores = font_small.render("Score: "+str(SCORE), True, BLACK)
    coins = font_small.render("Coins: "+str(COINS), True, BLACK)
    screen.blit(scores, (10,10))
    screen.blit(coins, (310, 10)) #Отображаем текущий счет (SCORE) и количество монет (COINS).

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()
    for entity in coins_s:
        screen.blit(entity.image, entity.rect)
        entity.move() #Проходимся по all_sprites и coins_s, отображаем каждый объект и перемещаем его.

    if pygame.sprite.spritecollideany(P1, enemies): #Проверяем столкновение игрока с врагами.
      
        pygame.mixer.Sound('Racer/Sounds/crash.wav').play()
        time.sleep(0.5)

        screen.fill(RED)
        screen.blit(game_over, (30,250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit() #Если да, проигрывается звук, отображается экран окончания игры, и программа завершается.

    if pygame.sprite.spritecollide(P1, coins_s, True):
        COINS += 1
        new_c = Coins()
        coins_s.add(new_c) #Если игрок собирает монету, счетчик монет увеличивается, а новая монета добавляется в группу.
        
        
            


    pygame.display.update() #Обновляем экран.


pygame.quit()
sys.exit() #После выхода из цикла, завершаем игру, закрывая окно.