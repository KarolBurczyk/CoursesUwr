# Karol Burczyk
# Program na zaliczenie przedmiotu Programowanie Obiektowe

import pygame


# klasa tła
class Background:

    # konstruktor klasy
    def __init__(self, scale):

        # wrzucenie skalę
        self.scale = scale

        # ładowanie grafiki
        bg = pygame.image.load('textures/bg.png')

        # skalowanie obrazu
        self.bg_img = pygame.transform.scale(bg,
                                             (bg.get_width() * self.scale, bg.get_height() * self.scale))

    # zwracamy grafikę tła
    def getBg(self):
        return self.bg_img

    # zwracamy szerokość grafiki tła
    def getWidth(self):
        return self.bg_img.get_width()

    # zwracamy wysokość tła
    def getHeight(self):
        return self.bg_img.get_height()


# klasa podłoża
class Ground:

    # konstruktor klasy
    def __init__(self, scale, screen_height):

        # wrzucenie skali
        self.scale = scale

        # załadowanie grafiki podłoża
        ground = pygame.image.load('textures/ground.png')

        # skalowanie obrazu
        self.ground_img = pygame.transform.scale(ground,
                                                 (ground.get_width() * self.scale, ground.get_height() * self.scale))

        # wyciągamy wymiary grafiki
        self.rect = self.ground_img.get_rect()

        # ustawiamy współrzędne grafiki w odpowiednim miejscu
        self.rect.top = screen_height - self.rect.height / 3

    # funkcja do zwracania grafiki podłoża
    def getGround(self):
        return self.ground_img

    # funkcja zwracająca szerokość grafiki
    def getWidth(self):
        return self.ground_img.get_width()

    # funkcja zwracająca wysokość grafiki
    def getHeight(self):
        return self.ground_img.get_height()

    # funkcja zwracająca wymiary i współrzędne podłoża
    def get_rect(self):
        return self.ground_img.get_rect()
