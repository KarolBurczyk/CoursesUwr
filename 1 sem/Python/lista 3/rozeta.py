from turtle import *
import random

pensize(2)
speed('fastest')

def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)

def rozeta(a, b, n):
    for j in range(n):
        fd(a)
        kwadrat(b)
        bk(a) #fd(-a)
        rt(360/n)

rozeta(100, 70, 10)

input()