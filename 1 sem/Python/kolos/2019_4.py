from turtle import *
speed('fastest')

def wczytaj_mape(plik):
    def kwadrat(x,y,kolor):
        pu()
        goto(x,y)
        pd()
        fillcolor(kolor)
        begin_fill()
        for i in range(4):
            fd(10)
            rt(90)
        end_fill()

    # mapa = open(plik).read().split()
    mapa = plik
    for y in range(len(mapa)):
        for x in range(len(mapa[y])):
            if mapa[y][x] == '.':
                kwadrat(x*10, -y*10, 'blue')
            else:
                kwadrat(x*10, -y*10, 'yellow')

a = ['....#....','..##....#','.....##..','.........']

wczytaj_mape(a)
