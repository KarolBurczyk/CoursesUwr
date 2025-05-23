from turtle import *
import random

slowa = open('Python/lista8/niespodzianka.txt', encoding="utf-8").read().split()
colormode(255)
speed('fastest')
#tracer(0,0)

def kwadrat(x, y, kolor):
    pu()
    goto(-x,-y)
    pd()
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(5)
        rt(90)
    end_fill()

def rysowanie():
    for i in range(20*len(slowa)):
        a = random.randint(0,len(slowa)-1)
        if slowa[a]!=0:
            kwadrat((a//52)*5, (a%52)*5, (eval(slowa[a])[0], eval(slowa[a])[1], eval(slowa[a])[2]))
            slowa[a] = 0 

rysowanie()
input()
#print(len(slowa)/63)