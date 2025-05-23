import matplotlib.pyplot as plt
import random 

# lista współrzędnych x i y
x_data = [0]
y_data = [0]
# stałe, które są wykorzystywane w czasie gry
_len = 8
sqr_count = 5

plt.ion()
fig, ax = plt.subplots()
# zdefiniowanie węża na wykresie
line, = ax.plot(x_data, y_data, linestyle = '-', linewidth = '1.5')

# wektory ruchów węża
choice = [[-1, 0], [1, 0], [0, 1], [0, -1]]
# wierzchołki kwadratów 
square = [[0, 0], [1, 0], [1, 1], [0, 1], [0, 0]]
squares = []

vector = random.choice(choice)
x_data.append(vector[0])
y_data.append(vector[1])

# losowanie miejsc kwadratów, dodawanie ich do wykresu oraz zapisywanie w tablicy squares
for i in range(sqr_count):
    x = random.randint(-9, 9)
    y= random.randint(-9, 9)
    squares.append([[v[0] + x, v[1] + y] for v in square[:-1]])
    ax.plot([v[0] + x for v in square], [v[1] + y for v in square], linestyle = '-', color = 'red', linewidth = '1.5')


def check_collisions():
    # sprawdzamy kolizje z własnym ogonem
    for i in range(len(x_data) - 1):
        if x_data[i] == x_data[-1] and y_data[i] == y_data[-1]:
            return True
    # sprawdzamy kolizje z kwadratami z tablicy squares
    for square in squares:
        for point in square:
            if point[0] == x_data[-1] and point[1] == y_data[-1]:
                return True

iterator = 3
while(1):

    line.set_xdata(x_data)
    line.set_ydata(y_data)

    # stałe ywmiary wykresu 20x20
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)

    plt.draw()
    if check_collisions():
        break

    # nie chcemy, żeby wąż robił ruch dokładnie odwrotny do poprzedniego oraz w przypadku dojścia do ściany zmieniał kierunek
    vector = random.choice([v for v in choice if (v != [-vector[0], -vector[1]] and abs(x_data[-1] + v[0]) <= 10 and abs(y_data[-1] + v[1]) <= 10)]) 
    # co klatkę dodajemy nową "głowę" węża
    x_data.append(x_data[-1] + vector[0])
    y_data.append(y_data[-1] + vector[1])

    # co _len nie usuwamy ostatniej części ogona, żeby wąż mógł rosnąć
    if iterator % _len != 0:
        x_data.pop(0)
        y_data.pop(0)

    # częstotliwość odświeżania
    plt.pause(0.2)
    iterator += 1

plt.ioff()
plt.show()
