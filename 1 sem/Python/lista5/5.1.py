from turtle import *
import random
speed('fastest')
colormode(255)

def kwadrat():
    fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    begin_fill()
    fd(30)
    rt(90)
    fd(30)
    rt(90)
    fd(30)
    rt(90)
    fd(30)
    rt(90)
    fd(30)
    rt(30)
    end_fill()

def trojkat():
    fillcolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    begin_fill()
    fd(30)
    rt(120)
    fd(30)
    rt(120)
    fd(30)
    rt(30)
    end_fill()

kwadrat()
trojkat()
for i in range(100):
    k = random.randint(0,2)
    if k==0 or k==1:
        kwadrat()
    else:
        rt(90)
        fd(30)
        rt(30)
        kwadrat()
    trojkat()


input()
