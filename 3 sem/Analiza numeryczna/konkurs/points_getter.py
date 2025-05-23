import pygame
import pickle

fileName = 'dane2.py'

class Game:
    def __init__(self):
        pygame.init()

        self.is_running = True
        self.window = pygame.display.set_mode((0,0), pygame.FULLSCREEN)

        pygame.display.set_caption("Points Getter")
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_CROSSHAIR)

        # otwarcie eksportu danych do pliku
        with open(fileName, 'w') as file:
            file.write(f"s = [\n")

        # upload i wycentrowanie grafiki napisu
        image = pygame.image.load("napis.png")
        bg = pygame.transform.scale(image, (image.get_width() * 1.5, image.get_height() * 1.5))
        rect = bg.get_rect()
        rect.center = (round(self.window.get_width()/2), round(self.window.get_height()/2))
        self.window.blit(bg, (rect.topleft))

        self.xs = []
        self.ys = []

        # główna pętla programu
        while self.is_running:
            self.update()
        pygame.quit()
        with open(fileName, 'a') as file:
            file.write(f"]")

    def update(self):
        pygame.display.update()
        self.check_events()

    # eksport współrzędnych punktów do pliku
    def export_data(self):
        with open(fileName, 'a') as file:
            file.write(f"{[self.xs, self.ys]},\n")

    def check_events(self):
        for ev in pygame.event.get():
            if ev.type == pygame.MOUSEBUTTONDOWN:
                # po kliknięciu myszką, dopisujemy kolejny punkt do tablicy 
                self.xs.append(pygame.mouse.get_pos()[0])
                self.ys.append(self.window.get_height() - pygame.mouse.get_pos()[1])
            if ev.type == pygame.QUIT:
                self.is_running = False
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.is_running = False
                    self.export_data()
                if ev.key == pygame.K_SPACE:
                    self.export_data()
                    self.xs.clear()
                    self.ys.clear()

    

if __name__ == '__main__':
    Game()
