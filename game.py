import pygame
import sys

# Инициализация Pygame
pygame.init()

# Определение цветов
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Определение размеров экрана
WIDTH, HEIGHT = 800, 600
FPS = 60

# Создание экрана
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rhythm Game")

# Определение основных переменных
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Класс кнопки
class Button(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()

# Функция рисования главного меню
def draw_main_menu():
    screen.fill(BLACK)
    text = font.render("Главное меню", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4 - text.get_height() // 2))

    # Здесь ты можешь добавить свой фон для меню, например:
    # background_image = pygame.image.load("your_background_image.png")
    # screen.blit(background_image, (0, 0))

    pygame.display.flip()

# Главное меню
def main_menu():
    in_main_menu = True

    while in_main_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    level_menu()
                elif event.key == pygame.K_2:
                    settings_menu()
                elif event.key == pygame.K_3:
                    pygame.quit()
                    sys.exit()

        draw_main_menu()
        clock.tick(FPS)

# Функция рисования меню выбора уровня
def draw_level_menu():
    screen.fill(BLACK)
    text = font.render("Выбор уровня", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4 - text.get_height() // 2))
    pygame.display.flip()

# Меню выбора уровня
def level_menu():
    in_level_menu = True

    while in_level_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    in_level_menu = False

        draw_level_menu()
        clock.tick(FPS)

# Функция рисования меню настроек
def draw_settings_menu():
    screen.fill(BLACK)
    text = font.render("Настройки", True, WHITE)
    # Добавь сюда отрисовку элементов настроек
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 4 - text.get_height() // 2))
    pygame.display.flip()

# Меню настроек
def settings_menu():
    in_settings_menu = True

    while in_settings_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    in_settings_menu = False

        draw_settings_menu()
        clock.tick(FPS)

if __name__ == "__main__":
    main_menu()
