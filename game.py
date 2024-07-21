import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Определение констант
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)

# Создание окна игры
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flying Rocket")

# Загрузка изображений
rocket_image = pygame.image.load("rocket.png")
obstacle_image = pygame.image.load("obstacle.png")
coin_image = pygame.image.load("coin.png")
space_image = pygame.image.load("space.jpg")

# Изменение размера космического фона
space_image = pygame.transform.scale(space_image, (WIDTH, HEIGHT))

# Получение размеров изображений
rocket_width, rocket_height = rocket_image.get_size()
obstacle_width, obstacle_height = obstacle_image.get_size()
coin_width, coin_height = coin_image.get_size()

# Позиция ракеты
rocket_x = WIDTH // 2 - rocket_width // 2
rocket_y = HEIGHT - rocket_height - 20

# Начальная скорость ракеты
rocket_speed = 10

# Список препятствий
obstacles = []

# Список монеток
coins = []

# Начальная скорость препятствий и монеток
obstacle_speed = 5
coin_speed = 5

# Счет игры
score = 0

# Часы для управления FPS
clock = pygame.time.Clock()

# Функция отрисовки ракеты
def draw_rocket(x, y):
    screen.blit(rocket_image, (x, y))

# Функция отрисовки препятствий
def draw_obstacles(obstacles):
    for obstacle in obstacles:
        screen.blit(obstacle_image, (obstacle[0], obstacle[1]))

# Функция отрисовки монеток
def draw_coins(coins):
    for coin in coins:
        screen.blit(coin_image, (coin[0], coin[1]))

# Функция отображения сообщения о поражении и запроса продолжения игры
def game_over():
    font = pygame.font.Font(None, 74)
    text = font.render("Game Over", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2))
    
    font_small = pygame.font.Font(None, 36)
    text_continue = font_small.render("Хотите продолжить игру?? (Y/N)", True, WHITE)
    screen.blit(text_continue, (WIDTH // 2 - text_continue.get_width() // 2, HEIGHT // 2 + text.get_height()))
    
    pygame.display.flip()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    return True
                elif event.key == pygame.K_n:
                    return False

# Главный цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Управление ракетой
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and rocket_x > 0:
        rocket_x -= rocket_speed
    if keys[pygame.K_RIGHT] and rocket_x < WIDTH - rocket_width:
        rocket_x += rocket_speed

    # Движение препятствий
    for obstacle in obstacles:
        obstacle[1] += obstacle_speed  # Скорость движения препятствия вниз
        if obstacle[1] > HEIGHT:
            obstacles.remove(obstacle)

    # Движение монеток
    for coin in coins:
        coin[1] += coin_speed  # Скорость движения монетки вниз
        if coin[1] > HEIGHT:
            coins.remove(coin)

    # Добавление нового препятствия с вероятностью 1%
    if random.randint(0, 100) == 0:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = 0 - obstacle_height
        obstacles.append([obstacle_x, obstacle_y])

    # Добавление новой монетки с вероятностью 2%
    if random.randint(0, 50) == 0:
        coin_x = random.randint(0, WIDTH - coin_width)
        coin_y = 0 - coin_height
        coins.append([coin_x, coin_y])

    # Проверка столкновения ракеты с препятствиями
    for obstacle in obstacles:
        if (
            rocket_x < obstacle[0] + obstacle_width
            and rocket_x + rocket_width > obstacle[0]
            and rocket_y < obstacle[1] + obstacle_height
            and rocket_y + rocket_height > obstacle[1]
        ):
            if not game_over():
                pygame.quit()
                sys.exit()
            else:
                # Сбросить позицию ракеты, препятствий и монеток
                rocket_x = WIDTH // 2 - rocket_width // 2
                rocket_y = HEIGHT - rocket_height - 20
                obstacles = []
                coins = []
                score = 0

    # Проверка сбора монеток
    for coin in coins:
        if (
            rocket_x < coin[0] + coin_width
            and rocket_x + rocket_width > coin[0]
            and rocket_y < coin[1] + coin_height
            and rocket_y + rocket_height > coin[1]
        ):
            score += 100
            coins.remove(coin)

    # Очистка экрана
    screen.blit(space_image, (0, 0))

    # Отрисовка ракеты, препятствий и монеток
    draw_rocket(rocket_x, rocket_y)
    draw_obstacles(obstacles)
    draw_coins(coins)

    # Отображение счета на экране
    font_score = pygame.font.Font(None, 36)
    text_score = font_score.render("Score: " + str(score), True, WHITE)
    screen.blit(text_score, (10, 10))

    # Обновление экрана
    pygame.display.flip()

    # Установка FPS
    clock.tick(FPS)
