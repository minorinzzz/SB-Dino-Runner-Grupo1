from dino_runner.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH
import pygame
FONT_STYLE = 'freesansbold.ttf'
#BLACK_RGB = (0, 0, 0)

def get_text_element(message, pos_x = SCREEN_WIDTH//2 , pos_y = SCREEN_HEIGHT //2, font_size = 30, color = (0,0,0)):
    font = pygame.font.Font(FONT_STYLE, font_size)

    text = font.render(message, True, color)
    text_rect = text.get_rect()
    text_rect.center = (pos_x, pos_y)

    return text, text_rect

