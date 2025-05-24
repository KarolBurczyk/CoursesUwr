# Karol Burczyk
# Program na zaliczenie przedmiotu Programowanie Obiektowe

import pygame


# klasa kolumny
class Tube:

    # konstruktor klasy, jako argumenty podajemy skalę, współrzędne x i y, odpowiednią grafikę oraz określenie czy
    # kolumna jest dolna, czy górna
    def __init__(self, scale, x, y, graphic, pos):

        # ładujemy obraz kolumny
        tube = pygame.image.load(graphic)

        # wczytujemy skalę
        self.scale = scale

        # skalujemy obraz
        self.tube_img = pygame.transform.scale(tube,
                                               (tube.get_width() * self.scale, tube.get_height() * self.scale))

        # wymiary zapisujemy pod zmienną rect
        self.rect = self.tube_img.get_rect()

        # ustawiamy współrzędne, zależnie od tego, czy jest to górna, czy dolna kolumna
        if pos == 'top':
            self.rect.midtop = (x, y)
        else:
            self.rect.midbottom = (x, y)

    # funkcja zwracająca grafikę kolumny
    def getTube(self):
        return self.tube_img

    # funkcja zwracająca szerokość kolumny
    def getWidth(self):
        return self.tube_img.get_width()

    # funkcja zwracająca wysokość kolumny
    def getHeight(self):
        return self.tube_img.get_height()

    # funkcja zwracająca wszystkie wymiary i współrzędne kolumny
    def get_rect(self):
        return self.tube_img.get_rect()
