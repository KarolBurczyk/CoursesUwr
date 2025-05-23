from turtle import *
import random
kolory = ['green', (0.5, 1, 0) , 'yellow', 'orange', 'red', (0.5, 0, 0) ]
tracer(0,0)

def colors(k):
    if k>0.85:   return (0.5, 0, 0)
    if k>0.65:   return 'red'
    if k>0.45:   return 'orange'
    if k>0.25:   return 'yellow'
    if k>0.15: return (0.5, 1, 0)
    else:   return 'green'

def wagi(k):
    if k>0.9:   return 1.35
    if k>0.7:   return 1.3
    if k>0.5:   return 1.25
    if k>0.3:   return 1.2
    else:   return 1

def wagii(k):
    return 1

t = [[0]*100 for i in range(100)]

def kwadrat(x,y, kolor):
    pu()
    goto(x*5-200, y*5-200)
    pd()
    k = colors(kolor)
    fillcolor(k)
    pencolor(k)
    begin_fill()
    for i in range(4):
        fd(5)
        rt(90)
    end_fill()

def losowanie(liczba_losowanie):
    for i in range(liczba_losowanie):
        x = random.randint(0,99)
        y = random.randint(0,99)
        t[x][y] = random.random()

def przypisywanie(liczba_przypisywanie):
    for i in range(liczba_przypisywanie):
        x = random.randint(1,98)
        y = random.randint(1,98)
        t[x][y] = (t[x+1][y]*wagi(t[x+1][y])+t[x-1][y]*wagi(t[x-1][y])+t[x][y+1]*wagi(t[x][y+1])+t[x][y-1]*wagi(t[x][y-1])+t[x+1][y+1]*wagi(t[x+1][y+1])+t[x-1][y-1]*wagi(t[x-1][y-1])+t[x+1][y-1]*wagi(t[x+1][y-1])+t[x-1][y+1]*wagi(t[x-1][y+1]))/8

def rysowanie():
    for i in range(1,99):
        for j in range(1,99):
            kwadrat(i, j, t[i][j])

losowanie(2500)
przypisywanie(70000)
rysowanie()
input()


