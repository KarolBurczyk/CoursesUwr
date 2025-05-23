from turtle import * 
import random

speed('fastest')

pu()
goto(0,-300)
pd()
lt(90)
fd(150)

def lisc():
    k=15
    lt(30)
    fd(k)
    rt(60)
    fd(k)
    rt(120)
    fd(k)
    rt(60)
    fd(k)
    rt(150)

def galaz(s):
    s=s-18
    k=random.randint(15,40)
    rt(k)
    fd(s)
    if s>50:
        galaz(s)
    else:
        lisc()
    fd(-s)
    lt(k)
    k=random.randint(15,40)
    lt(k)
    fd(s)
    if s>50:
        galaz(s)
    else:
        lisc()
    fd(-s)
    s=s+20
    rt(k)
    

galaz(150)
input()       