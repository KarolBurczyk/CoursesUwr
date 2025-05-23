# Karol Burczyk
# Program na zaliczenie przedmiotu Programowanie Obiektowe

import pygame
from CONST import *


# klasa postaci
class Bird:

    # do konstruktora podajemy skalę i pozycję, w której będzie wyświetlany ptak
    def __init__(self, scale, pos):

        # ładujemy grafikę ptaka
        bird = pygame.image.load('textures/bird_sing.png')

        # wrzucamy skalę
        self.scale = scale

        # skalujemy obraz
        self.bird_img = pygame.transform.scale(bird,
                                               (bird.get_width() * self.scale, bird.get_height() * self.scale))

        # zbieramy wymiary grafiki
        self.rect = self.bird_img.get_rect()

        # zmniejszamy szerokość obiektu, żeby lepiej działały kolizje
        self.rect.width *= 0.8

        # ustawiamy współrzędne ptaka
        self.rect.center = pos

        # przesuwamy współrzędną x o 1/2 szerokości ptaka
        self.rect.x += self.bird_img.get_width() / 2

    # funkcja zwiększająca wysokość ptaka
    def up(self):
        self.rect.y -= BIRD_JUMP

    # analogiczna funkcja zmniejszająca jego wysokość
    def down(self):
        self.rect.y += BIRD_FALL

    # funkcja zwracająca grafikę postaci
    def get_character(self):
        return self.bird_img

    # funkcja do zmiany pozycji ptaka
    def set_character(self, x, y):
        self.rect.center = (x, y)
        self.rect.x += self.bird_img.get_width() / 2