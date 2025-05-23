from turtle import pensize, pencolor, fd, bk, rt ,lt, speed
import random

pensize(4)
speed('fastest')

n = 500
d = 10
r = 55

kolory = ['green' , 'red' , 'blue' , 'pink']
for i in range(n):
    kolor= random.choice(kolory)
    pencolor(kolor)
    fd(d)
    rt(random.randint(-r,r))

input()

