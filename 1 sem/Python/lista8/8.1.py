from turtle import *
import random

slowa = open('Python/lista8/niespodzianka.txt', encoding="utf-8").read().split()
colormode(255)
tracer(0,0)

def kwadrat(y, x, kolor):
    pu()
    goto(-x+260,-y+230)
    pd()
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(12)
        rt(90)
    end_fill()

def rysowanie():
    i=0
    for y in range(63):
        for x in range(52):
            kwadrat(x*10, y*10, (eval(slowa[i])[0], eval(slowa[i])[1], eval(slowa[i])[2]))
            i+=1

rysowanie()
input()
#print(len(slowa)/63)