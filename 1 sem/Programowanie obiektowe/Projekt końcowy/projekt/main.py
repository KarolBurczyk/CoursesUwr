# Karol Burczyk
# Program na zaliczenie przedmiotu Programowanie Obiektowe
# Gra Flappy Bird w mojej interpretacji

# import klas z innych plików oraz potrzebnych bibliotek
import math
import random
import pygame
from character import Bird
from scene import Background, Ground
from tubes import Tube
from CONST import *


# główna klasa gry
class Game:

    # konstruktor klasy Game
    def __init__(self):

        # inicjacja pygame
        pygame.init()

        # poniższe wartości typu bool służą do rozpoznawania, w którym momencie gry jesteśmy

        # is_running informuje pętlę główną gry, że ma dalej być uruchomiona
        self.is_running = True

        # is_playing zmieni się na True, gdy zaczniemy grać
        self.is_playing = False

        # game_over zmieni się na True, gdy zahaczymy, o którąś z przeszkód
        self.game_over = False

        # wartość informująca o ty czy jesteśmy w menu, na początku ustawiona na prawdę
        self.menu = True

        # pozycja myszki
        self.mouse = pygame.mouse.get_pos()

        # definicja okna gry o określonej rozdzielczości
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        # ustawienie tytułu okna gry na Flappy Bird
        pygame.display.set_caption("Flappy Bird")

        # szerokość okna gry
        self.screen_width = self.window.get_width()

        # wysokość ona gry
        self.screen_height = self.window.get_height()

        # wyliczam skalę grafik w grze (stosunek ustawionej wysokości ekranu do wysokości grafiki tła)
        self.scale = self.screen_height / BG_HEIGHT

        # ustawienie czcionki do punktów
        self.font = pygame.font.Font('./Font.ttf', 72)

        # ustawienie czcionki do listy wyników
        self.scores_font = pygame.font.Font('./Font.ttf', 25)

        # wywołanie obiektu tła gry dla odpowiedniej skali
        self.bg = Background(self.scale)

        # wywołanie obiektu podłoża dla skali i wysokości ekranu
        self.ground = Ground(self.scale, self.screen_height)

        # wywołanie obiektu ptaka dla skali oraz pozycji początkowej na ekranie
        self.bird = Bird(self.scale, (self.screen_width // 4, self.screen_height / 2))

        # listy kolumn górnych i dolnych
        self.tubes = []
        self.tubes2 = []

        # definicja licznik kolumn
        self.tubes_counter = 1

        # określenie częstotliwości wyświetlania kolumn
        self.tubes_freq = 0.1

        # określenie prędkości przesuwania się kolumn i podłoża
        self.speed = 8

        # określenie prędkości paralaksy (jak szybko będzie się przesuwać tło)
        self.parallax_speed = 4

        # ustawienie poziomu trudności (jak wąska szpara zostanie między kolumnami)
        self.difficulty_lvl = 0.3

        # definicja przesuwania tła, podłoża i kolumn
        self.scroll_bg = 0
        self.scroll_ground = 0
        self.scroll_tubes = 0

        # określenie ile grafik podłoża/tła musimy wyświetlić, żeby zapełniły szerokość ekranu
        self.tiles = math.ceil(self.screen_width / self.bg.getWidth()) + 1

        # wyzerowany na starcie licznik punktów
        self.points_counter = 0

        # do obydwu list dodajemy po jednej kolumnie (pierwszej, która się wyświetli)
        # wywołujemy obiekt kolumny dla odpowiedniej skali, szerokości ekranu, losowej wysokości wyliczanej na
        # podanym przedziale, odpowiedniej tekstury (górnej albo dolnej) oraz określenia jej pozycji jako top lub
        # bottom
        self.tubes.append(Tube(self.scale, self.screen_width,
                               random.randint(round(self.screen_height * 0.3), round(self.screen_height
                                                                                     * 0.7)), 'textures/tube2.png',
                               'top'))

        # analogicznie dodajemy do drugiej listy obiekt kolumny, tylko wywołany dla argumentów dla kolumny dolnej
        self.tubes2.append(Tube(self.scale, self.screen_width,
                                self.tubes[0].rect.midtop[1] - round(self.screen_height * self.difficulty_lvl),
                                'textures/tube1.png', 'bottom'))

        # zdefiniowanie zegara (funkcja pygame)
        self.clock = pygame.time.Clock()

        # główna pętla gry składa się tylko z funkcji update i działa, dopóki is_running jest prawdą
        while self.is_running:
            self.update()

        # w innym wypadku kończymy grę
        pygame.quit()

    # funkcja do wyświetlania naszego bohatera na ekranie
    def draw_bird(self):

        # wykonujemy tick zegara
        self.clock.tick(CLOCK_TICK)

        # wyświetlamy na ekranie grafikę ptaka (szerokość, na której jest wyświetlany, będzie stała, wysokość
        # jest aktualizowana na bieżąco)
        self.window.blit(self.bird.get_character(), (self.screen_width // 4, self.bird.rect.y))

    # funkcja do wyświetlania tła, zanim gra się rozpocznie
    def draw_start_background(self):

        # wyświetlamy odpowiednią liczbę obrazków (tę liczbę wyliczaliśmy w konstruktorze
        for i in range(self.tiles):
            # jako parametry do wyświetlenia jest oczywiście grafika, szerokość (wyświetlamy i-ty element) oraz
            # wysokość równa 0
            self.window.blit(self.bg.getBg(), (i * self.bg.getWidth(), 0))

    # funkcja do wyświetlania podłoża, zanim gra się rozpocznie
    def draw_start_ground(self):

        # wyświetlamy odpowiednią liczbę obrazków (tę liczbę wyliczaliśmy w konstruktorze
        for i in range(self.tiles):
            # podajemy obiekt graficzny podłoża, odpowiednia szerokość oraz wyliczoną wysokość
            self.window.blit(self.ground.getGround(),
                             (i * self.ground.getWidth(), self.screen_height - self.ground.getHeight() / 3))

    # w tej funkcji będziemy wyświetlać tło w czasie działania gry
    def draw_game_bg(self):

        # wykonujemy tick zegara
        self.clock.tick(CLOCK_TICK)

        # wyświetlamy odpowiednią liczbę "kafelków" tła, szerokość jest zawsze odpowiednio powiększana o wartość
        # scroll_bg, którą po każdym wyświetleniu pomniejszamy o wartość parallax_speed
        i = 0
        while i < self.tiles:
            self.window.blit(self.bg.getBg(), (self.bg.getWidth() * i
                                               + self.scroll_bg, 0))
            i += 1

        self.scroll_bg -= self.parallax_speed

        # kiedy wartość scroll_bg przekroczy szerokość jednego kafelka, ustawiamy ją z powrotem na 0
        if abs(self.scroll_bg) > self.bg.getWidth():
            self.scroll_bg = 0

    # analogiczna funkcja jak powyższa, która wyświetla podłoże
    def draw_game_ground(self):

        self.clock.tick(CLOCK_TICK)

        i = 0
        while i < self.tiles:
            self.window.blit(self.ground.getGround(), (self.ground.getWidth() * i
                                                       + self.scroll_ground,
                                                       self.screen_height - self.ground.getHeight() / 3))
            i += 1

        self.scroll_ground -= self.speed

        if abs(self.scroll_ground) > self.ground.getWidth():
            self.scroll_ground = 0

    # funkcja do wyświetlania kolumn na ekranie
    def draw_tubes(self):

        # wykonujemy tick zegara
        self.clock.tick(CLOCK_TICK)

        # dla każdego elementu z listy kolumn górnych wyświetlamy ją na ekranie
        for element in self.tubes:
            self.window.blit(element.getTube(), (element.rect.x, element.rect.y))

            # następnie pomniejszamy jej współrzędną x o wartość speed
            element.rect.x -= self.speed

        # analogiczna funkcja dla kolumn dolnych
        for element in self.tubes2:
            self.window.blit(element.getTube(), (element.rect.x, element.rect.y))
            element.rect.x -= self.speed

        # jeżeli wartość przesunięcia dla kolumn będzie większa od połowy szerokości kafelka podłoża
        # (pomnożonego razy ilość kolumn)
        if abs(self.scroll_tubes) >= self.ground.getWidth() * self.tubes_counter / 2:
            # w takim wypadku dodajemy do listy nowy obiekt kolumny dla odpowiednich parametrów
            self.tubes.append(Tube(self.scale, self.screen_width + self.tubes_counter * self.ground.getWidth() *
                                   self.tubes_freq, random.randint(round(self.screen_height * 0.35),
                                                                   round(self.screen_height * 0.8)),
                                   'textures/tube2.png', 'top'))

            # dodajemy analogicznie element do listy kolumn dolnych (jego wysokość jest wyliczana
            # na podstawie wysokości górnej, która będzie nad nią)
            self.tubes2.append(Tube(self.scale, self.screen_width + self.tubes_counter * self.ground.getWidth() *
                                    self.tubes_freq, self.tubes[len(self.tubes) - 1].rect.midtop[1] - round(
                self.screen_height * self.difficulty_lvl), 'textures/tube1.png', 'bottom'))

            # na koniec zwiększamy licznik kolumn
            self.tubes_counter += 1

        # pomniejszamy przesunięcie kolumn o wartość speed
        self.scroll_tubes -= self.speed

    # funkcja wyświetlająca aktualną liczbę punków na ekranie
    def draw_points(self, points):

        # tworzymy tekst dla wcześniej ustawionej czcionki
        text = self.font.render(str(points), True, 'black')

        # tworzymy zestaw współrzędnych i wymiarów tekstu
        text_rect = text.get_rect()

        # ustawiamy współrzędne środka naszego tekstu
        text_rect.center = (self.screen_width // 12, self.screen_height // 8)

        # wyświetlamy tekst na ekranie
        self.window.blit(text, text_rect)

    # funkcja zapisująca wynik do pliku
    def save_score(self, points):

        # otwieramy plik w trybie 'a' (append) i zapisujemy nasze punkty
        with open('high_scores.txt', 'a') as file:
            file.write(str(points) + '\n')

    # funkcja zapisująca wynik do pliku
    def get_scores(self):

        # otwieramy plik w trybie 'r' (read) i odczytujemy nasze punkty
        with open('high_scores.txt', 'r') as file:
            lines = file.readlines()

        # konwertowanie wartości na liczby całkowite
        values = [int(line.strip()) for line in lines]

        # sortowanie wartości w kolejności malejącej
        sorted_values = sorted(values, reverse=True)

        # zwracanie 10 największych wartości (lub mniej, jeśli jest ich mniej niż 10)
        return sorted_values[:15]

    # funkcja sprawdzająca, czy zachodzi kolizja między obiektami
    def check_collisions(self):

        # jeżeli zachodzi kolizja ptaka z podłożem gra się kończy
        if self.bird.rect.colliderect(self.ground.rect):
            self.game_over = True

        # jeżeli ptak wejdzie w kolizję z najbliższą kolumną to gra się również kończy
        if self.bird.rect.x + self.bird.rect.width >= self.tubes[self.points_counter].rect.x and \
                self.bird.rect.x <= self.tubes[self.points_counter].rect.x + self.tubes[self.points_counter].rect.width:
            if self.bird.rect.y + self.bird.rect.height >= self.tubes[self.points_counter].rect.midtop[1] or \
                    self.bird.rect.y <= self.tubes2[self.points_counter].rect.midbottom[1]:
                self.game_over = True

                # zapisanie wyniku do pliku
                self.save_score(self.points_counter)

    # funkcja restartu gry w przypadku przegrania poprzedniej sesji
    def restart(self):

        # is_running dalej jest prawdziwe, ponieważ nie zamykamy gry
        self.is_running = True

        # is_playing ustawiamy na false
        self.is_playing = False

        # game_over przyjmuje wartość pozytywną
        self.game_over = False

        # ustawiamy pozycję ptaka na wyjściową
        self.bird.set_character(self.screen_width / 4, self.screen_height / 2)

        # czyścimy listę kolumn
        self.tubes = []
        self.tubes2 = []

        # ustawiamy licznik kolumn na 1
        self.tubes_counter = 1

        # zmieniamy wartości prędkości na początkowe
        self.speed = 8
        self.parallax_speed = 4
        self.difficulty_lvl = 0.3

        # to samo robimy z wartościami przesunięcia i licznikiem punktów
        self.scroll_bg = 0
        self.scroll_ground = 0
        self.scroll_tubes = 0
        self.points_counter = 0

        # dodajemy z powrotem po jednej kolumnie do obydwu list
        self.tubes.append(Tube(self.scale, self.screen_width,
                               random.randint(round(self.screen_height * 0.3), round(self.screen_height
                                                                                     * 0.7)), 'textures/tube2.png',
                               'top'))

        self.tubes2.append(Tube(self.scale, self.screen_width,
                                self.tubes[0].rect.midtop[1] - round(self.screen_height * self.difficulty_lvl),
                                'textures/tube1.png', 'bottom'))

    # funkcja sprawdzająca zachodzące wydarzenia w czasie gry
    def check_events(self):

        # dla każdego wydarzenia zachodzącego w grze:
        for ev in pygame.event.get():

            # jeżeli nastąpi wciśnięcie przycisku:
            if ev.type == pygame.KEYDOWN:

                # jeżeli wciskamy przycisk ESC i jesteśmy w menu, następuje wyjście z gry
                if ev.key == pygame.K_ESCAPE:
                    if self.menu:
                        self.is_running = False

                    # w innym przypadku wracamy do menu
                    else:
                        self.restart()
                        self.menu = True

                # jeżeli wciskamy spację
                if ev.key == pygame.K_SPACE:

                    # jeżeli nie rozpoczęliśmy jeszcze gry, to uruchamiamy ją w tym momencie
                    if not self.game_over and not self.is_playing and not self.menu:
                        self.is_playing = True

                    # w przypadku wcześniejszej kolizji postaci następuje restart gry
                    if self.game_over and not self.menu:
                        self.restart()

            # jeżeli zostanie wciśnięty przycisk na myszce i jesteśmy w menu
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if self.menu:

                    # sprawdzamy, czy pozycja myszki pokrywa się z przyciskiem uruchomienia gry, wtedy zamykamy
                    # sekcję menu i przechodzimy do rozgrywki
                    if self.screen_width / 2 - 64 * self.scale <= self.mouse[
                        0] <= self.screen_width / 2 + 64 * self.scale \
                            and self.screen_height / 2 - 64 * self.scale <= self.mouse[1] <= self.screen_height / 2 \
                            + 64 * self.scale:
                        self.menu = False

            # jeżeli zachodzi wydarzenie QUIT, to gra się zamyka
            if ev.type == pygame.QUIT:
                self.is_running = False

        # w czasie gry wciśnięcie spacji powoduje lot w górę postaci
        if pygame.key.get_pressed()[pygame.K_SPACE] and not self.game_over and self.is_playing and not self.menu:
            self.bird.up()

        # jeżeli postać przekroczy kolejną kolumnę, to zwiększamy punkty
        if self.bird.rect.bottomleft[0] > self.tubes[self.points_counter].rect.topright[0]:
            self.points_counter += 1

            # a jeżeli przekroczymy kolejne 5 punktów, wzrasta poziom trudności oraz prędkość przesuwania ekranu
            if self.points_counter % 5 == 0:
                self.difficulty_lvl *= 0.9
                self.speed += 0.5
                self.parallax_speed += 0.5

    # jeżeli przegramy sesję, wyświetlany jest napis "game_over"
    def draw_game_over(self):
        over = pygame.image.load('textures/game_over.png')
        over_img = pygame.transform.scale(over,
                                          (over.get_width() * self.scale, over.get_height() * self.scale))
        rect = over_img.get_rect()
        rect.center = (self.screen_width / 2, self.screen_height / 2)
        self.window.blit(over_img, rect)

    # funkcja wyświetlająca grafikę ze strzałką, której kliknięcie uruchamia rozgrywkę
    def draw_play_button(self):
        play = pygame.image.load('textures/play.png')
        play_img = pygame.transform.scale(play,
                                          (play.get_width() * self.scale, play.get_height() * self.scale))
        rect = play_img.get_rect()
        rect.center = (self.screen_width / 2, self.screen_height / 2)
        self.window.blit(play_img, rect)

    # funkcja do rysowania na ekranie tablicy z najwyższymi wynikami
    def draw_highscore(self):

        # ładowanie grafiki kartki
        scores = pygame.image.load('textures/highscores.png')

        # skalowanie obrazu
        scores_img = pygame.transform.scale(scores,
                                            (scores.get_width() * self.scale * 0.7, scores.get_height() * self.scale))

        # pobieramy wymiary grafiki
        rect = scores_img.get_rect()

        # ustawiamy jej współrzędne
        rect.center = (self.screen_width * 0.85, self.screen_height * 0.35)

        # na koniec wyświetlamy na ekranie
        self.window.blit(scores_img, rect)

        # render tekstu "hisghscores"
        text = self.scores_font.render("Highscores", True, 'black')

        # tworzymy zestaw współrzędnych i wymiarów tekstu
        text_rect = text.get_rect()

        # ustawiamy współrzędne środka naszego tekstu
        text_rect.center = (self.screen_width * 0.84, self.screen_height * 0.1)

        # wyświetlamy tekst na ekranie
        self.window.blit(text, text_rect)

        # pobieramy wyniki z pliku za pomocą funkcji
        scores = self.get_scores()

        # ustawiamy wysokość pierwszego wyniku i pierwszy numer
        height = self.screen_height * 0.16
        i = 1

        # dla każdego wyniku:
        for score in scores:

            # tworzymy nowy tekst z naszym pojedynczym wynikiem
            text = self.scores_font.render(str(i) + "." + "     " + str(score), True, 'black')

            # tworzymy zestaw współrzędnych i wymiarów tekstu
            text_rect = text.get_rect()

            # ustawiamy współrzędne środka naszego tekstu
            text_rect.center = (self.screen_width * 0.84, height)

            # wyświetlamy tekst na ekranie
            self.window.blit(text, text_rect)

            # zwiększamy wartość wysokości dla następnego wyniku i jego numer
            height += self.screen_height * 0.03
            i += 1

    # funkcja update odpowiadająca za wszystkie aktualizacje obrazu gry
    def update(self):

        # na początek aktualizujemy pygame
        pygame.display.update()

        # na początku gry uruchamiać się będzie menu, które uruchamia poniższe funkcje
        if self.menu:
            self.draw_start_background()
            self.draw_start_ground()
            self.draw_play_button()
            self.draw_highscore()
            # aktualizujemy pozycję myszki
            self.mouse = pygame.mouse.get_pos()
            self.check_events()

        # jeżeli przegraliśmy, rysujemy tło, podłoże i postać w wyjściowej pozycji
        elif self.game_over and not self.menu:
            self.draw_bird()
            self.draw_game_over()
            self.check_events()

        # jeżeli jeszcze nie gramy, to wyświetlamy wszystkie obiekty w wyjściowej pozycji
        elif not self.is_playing:
            self.draw_start_background()
            self.draw_start_ground()
            self.draw_bird()
            self.check_events()

        # w czasie gry wywołujemy wszystkie funkcje dotyczące wyświetlania i aktualizowania informacji w czasie
        # rozgrywki
        else:
            self.check_collisions()
            self.check_events()
            self.draw_game_bg()
            self.draw_tubes()
            self.draw_game_ground()
            self.draw_bird()
            self.bird.down()

            # jeżeli przegramy, to zmniejszamy wysokość postaci o 10, żeby zapobiec duplikowaniu grafiki
            if self.game_over:
                self.bird.rect.y -= 10

        # na koniec wyświetlamy aktualną liczbę punktów
        self.draw_points(self.points_counter)


# gdy uruchamiamy program, wywołujemy obiekt klasy głównej Game
if __name__ == '__main__':
    Game()
