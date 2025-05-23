from turtle import *

bok = 15
sx = -100
sy = 0

plansza = '''
..............................
..............................
...............#####..........
...........######.............
..............................
.........................#....
.........................##...
...........########.......#...
...........###..####..........
...........######.............
...........##.................
..............................
...................####.......
..............................
'''

my = len(plansza)
mx = len(plansza[0])

def kwadrat(x , y, kolor):
    fillcolor(kolor)
    pu()
    goto( sx + x * bok, sy + y * bok)
    pd()
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

kierunki = [(1,0), (-1,0), (1,1), (-1,1), (1,-1), (0,1), (0,-1), (-1,-1)]

def liczba_sasiadow(x, y):
    ls = 0
    for dx, dy in kierunki:
        nx = (x + dx) % mx
        ny = (y + dy) % my
        if plansza[ny][nx] == '#':
            ls +=1
    return ls


def przemiana(plansza):
    for i in range(len(mx)):
        for j in range(len(my)):
            ls = liczba_sasiadow(i, j)
            if plansza[i][j]=='#':
                if ls != 2 or ls != 3:
                    plansza[i][j]=='.'
            else:
                



