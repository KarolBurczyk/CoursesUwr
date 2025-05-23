from duze_cyfry import daj_cyfre
from turtle import *
import random

speed('fastest')
pensize(2)
colormode(255)


def kwadrat(kolor):
    colormode(255)
    fillcolor(kolory[kolor], kolory[kolor+1], kolory[kolor+2])
    begin_fill()
    lt(90)
    fd(20)
    lt(90)
    fd(20)
    lt(90)
    fd(20)
    lt(90)
    fd(20)
    end_fill()


k = 8567
s=[]
kolory=[]
while k>0:
    s.append(k%10)
    kolory.append(random.randint(0,255))
    kolory.append(random.randint(0,255))
    kolory.append(random.randint(0,255))
    k//=10

int(s[len(s)-1]) 
l=len(s)-1

pu()
rt(180)
fd(300)
rt(180)
pd()
for i in range(5):
    for j in range(l+1):
        for k in range(5):
            if daj_cyfre(int(s[l-j]))[i][k] == '#':
                kwadrat((l-j)*3)
            pu()
            fd(20)
            pd()
        pu()
        fd(20)
        pd()
    pu()
    rt(90)
    fd(20)
    rt(90)
    fd(20*len(s)*6)
    rt(180)
    pd()

input()

