from turtle import *
import random

bok = 30
speed('fastest')

def move(x,y): #przemieszczanie sie bez
    penup() #w skrocie pu
    goto(x,y)
    pendown() #w skrocie pd

def kwadrat(x, y, bok): 
    move(x, y)
    colormode(255)
    fillcolor()
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()
move(-15,-15)
for i in range(400):
    bok = 30
    kwadrat (random.randint(-12,12)*bok, random.randint(-12,12)*bok, bok)

#t = Turtle()
#r = 100
#t.circle(r)

input()