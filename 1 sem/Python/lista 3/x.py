from turtle import *
import random

bok = 30
speed('fastest')

def move(x,y):
    penup() #w skrocie pu
    goto(x,y)
    pendown() #w skrocie pd

def kwadrat(x, y, bok): 
    move(x, y)
    colormode(255)
    fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()

for i in range(500):
    bok = random.randint(20,100)
    kwadrat (random.randint(-700,700), random.randint(-400,400), bok)

#t = Turtle()
#r = 100
#t.circle(r)

input()