from duze_cyfry_7 import daj_cyfre
from turtle import *
import random

kolory = ['red', 'blue', 'orange', 'yellow', 'green', 'pink', 'cyan']
t = [[' '] * 52 for i in range(52)]
speed('fastest')
tracer(0,0)

def kwadrat(kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(10)
        rt(90)
    end_fill()

def czywolne(x, y, cyfra, kolor):
    for i in range(5):
        for j in range(5):
            if cyfra[i][j]=='#' and t[x+i][y+j]!=' ':
                return 0
            elif t[x+i+1][y+j]==kolor or t[x+i-1][y+j]==kolor or t[x+i][y+j+1]==kolor or t[x+i][y+j-1]==kolor:
                return 0
    return 1

def rysowanie(x, y, cyfra, kolor):
    for i in range(5):
        for j in range(5):
            if cyfra[i][j]=='#':
                t[x+i][y+j]=kolor

def zolw():
    pu()
    fd(-320)
    lt(90)
    fd(220)
    rt(90)
    pd()
    for i in range(1,51):
        for j in range(1,51):
            if t[i][j]!=' ':
                pd()
                kwadrat(t[i][j])
            pu()
            fd(10)
        fd(-50*10)
        rt(90)
        fd(10)
        lt(90)

def main():
    for k in range(200):
        x = random.randint(1,46)
        y = random.randint(1,46)
        cyfra = daj_cyfre(random.randint(0,9))
        kolor = random.choice(kolory)
        if czywolne(x, y, cyfra, kolor)==1:
            rysowanie(x, y, cyfra, kolor)

main()
zolw()
input()