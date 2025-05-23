import pygame
from CONST import *


# klasa Button
class Button:
    def __init__(self, pos, text, scale):
        self.scale = scale
        smallfont = pygame.font.SysFont(text, 35)
        text = smallfont.render('quit', True, 'black')
        button = pygame.image.load('textures/button.png')
        button_img = pygame.transform.scale(button,
                                          (button.get_width() * self.scale, button.get_height() * self.scale))
        rect = button_img.get_rect()
        rect.center = pos

