import pygame #Импортируем библиотеку pygame, которая предоставляет функции для работы с мультимедиа, графикой и обработкой событий.

pygame.init() #инициализирует все модули Pygame.
running = True #флаг для работы основного цикла программы.
WIDTH, HEIGHT = 1200, 800 #задает ширину и высоту окна приложения.
FPS = 60 #устанавливает частоту кадров (frames per second), т.е. как часто обновляется экран.

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #создает окно с указанными размерами.
pygame.display.set_caption("Paint") #устанавливает название окна "Paint".
clock = pygame.time.Clock() #создает объект часов для контроля времени (например, чтобы ограничить FPS).

rectangular = pygame.Rect(10, 10, 20, 10) #создает прямоугольник для выбора формы. Он отображается на панели меню.
circle_radius = 10 #радиус круга, который также будет на панели.
circle_center = (50, 20) #центр круга на панели.
pos = (1200, 800) #переменная для позиции мыши.


blue = pygame.Rect(1090, 10, 20, 20)
red = pygame.Rect(1130, 10, 20, 20)
green = pygame.Rect(1170, 10, 20, 20) #Создаем прямоугольники, представляющие цвета синим, красным и зеленым на панели управления.

color = "white" #начальный цвет кисти (по умолчанию белый).
shape = "rectangular" #начальная форма кисти (по умолчанию прямоугольник).

eraser = pygame.image.load("Paint/eraser.png") #загружает изображение ластика.
eraser_rect = eraser.get_rect() #создает объект прямоугольника, ограничивающий изображение ластика.
eraser_rect.center = (1050, 15) #задает положение центра ластика на панели.

do_draw = False #флаг, указывающий, рисует ли программа в данный момент.
drawings = []  #список для хранения всех нарисованных элементов (их цвета, формы и позиции).


def handler():
    global pos, do_draw
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #если окно закрыто, возвращает False для завершения цикла.
            return False
        if event.type == pygame.MOUSEBUTTONDOWN: #при нажатии левой кнопкой мыши (event.button == 1), активируется рисование.
            if event.button == 1:
                do_draw = True
                pos = pygame.mouse.get_pos()   
        if event.type == pygame.MOUSEMOTION: #при движении мыши обновляется позиция pos, если do_draw включен.
            if do_draw:
                pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONUP: #отключает рисование при отпускании кнопки мыши.
            do_draw = False
    return True


def menu():
    pygame.draw.aaline(screen, "black", (0, 40), (1200, 40))
    pygame.draw.rect(screen, "black", rectangular)
    pygame.draw.circle(screen, "black", circle_center, circle_radius)
    screen.blit(eraser, eraser_rect.center)
    pygame.draw.rect(screen, "blue", blue)
    pygame.draw.rect(screen, "red", red) #Линия разделяет панель меню от области рисования.
    pygame.draw.rect(screen, "green", green) #Прямоугольник, круг, ластик и кнопки с цветами отображаются в соответствующих позициях.

    

def choose_shape(pos):
    global shape
    if rectangular.collidepoint(pos): #Если нажата кнопка rectangular, форма меняется на прямоугольник.
        shape = "rectangular"
    elif ((circle_center[0] - pos[0])**2 + (circle_center[1] - pos[1])**2) <= circle_radius**2: #Если круг, то меняется на круг.
        shape = "circle"
    elif eraser_rect.collidepoint(pos): #Если ластик, возвращается прямоугольная форма (для "стирания").
        shape = "rectangular"


def choose_color(pos):
    global color
    if red.collidepoint(pos):
        color = "red"
    if blue.collidepoint(pos):
        color = "blue"
    if green.collidepoint(pos):
        color = "green"
    if eraser_rect.collidepoint(pos):
        color = "white" #Эта функция проверяет, на какой цвет нажали, и обновляет цвет кисти.


def active(color, shape):
    if shape == "rectangular":
        pygame.draw.rect(screen, color, (600, 10, 20, 10))
    elif shape == "circle":
        pygame.draw.circle(screen, color, (605, 18), 10) #Показывает текущие цвет и форму в верхней части экрана.


def drawing(color, shape, pos = pos):
    if pos[1] > 40:
        if shape == "rectangular":
            pygame.draw.rect(screen, color, [pos[0], pos[1], 20, 10])
        elif shape == "circle":
            pygame.draw.circle(screen, color, pos, 10) #Если позиция мыши ниже 40 (ниже панели меню), функция рисует прямоугольник или круг в зависимости от активной формы и цвета.



while running:
    clock.tick(FPS) #поддерживает частоту кадров.
    screen.fill("white")  #заполняет фон белым цветом.
    running = handler() #проверяет события.
    menu() #отображает меню.
    choose_shape(pos)
    choose_color(pos) #обновляют активную форму и цвет.
    active(color, shape) #показывает выбранные форму и цвет.
    
    for art in drawings: #отрисовывает все элементы из памяти drawings.
        drawing(art[0], art[1], art[2]) 
    drawing(color, shape, pos) #рисует текущий элемент.
    drawings.append((color, shape, pos)) #добавляет текущий элемент в память.

    





    pygame.display.update() #обновляет экран.



pygame.quit() #завершает Pygame, закрывая приложение.