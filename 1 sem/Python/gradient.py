import random
from turtle import *
import numpy as np

def move(x, y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(x, y, bok, kolor):
    move(x, y)
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()   
  
speed('fastest')    

kolor1 = np.array([1, 0.4, 0.5])
kolor2 = np.array([0.3, 0.1, 1])

N = 10
BOK = 50

for i in range(N+1):
    alfa = i / N
    mieszanka = (1-alfa) * kolor1 + alfa * kolor2
    kwadrat(-200 + BOK * i,0,  BOK, mieszanka)

input()