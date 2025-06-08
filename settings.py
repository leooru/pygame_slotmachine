#all settings
import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
LIGHTGRAY = (200, 200, 200)


user_text = ""
input_text = ""
check_text = True
icon_size = (90, 90)  # Einheitliche Größe für alle Icons


def render_text(text, color, x, y, size, fenster, rendered_text):
    font_x = pygame.font.SysFont(None, size)
    rendered_text = font_x.render(text, True, color)
    fenster.blit(rendered_text, (x, y))

icon_dict = {
    "apple": pygame.transform.scale(pygame.image.load("Assets/icons/apple.png"), icon_size),
    "banana": pygame.transform.scale(pygame.image.load("Assets/icons/banana.png"), icon_size),
    "book": pygame.transform.scale(pygame.image.load("Assets/icons/book.png"), icon_size),
    "cherry": pygame.transform.scale(pygame.image.load("Assets/icons/cherry.png"), icon_size),
    "seven": pygame.transform.scale(pygame.image.load("Assets/icons/seven.png"), icon_size)
}