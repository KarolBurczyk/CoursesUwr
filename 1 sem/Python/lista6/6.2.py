from turtle import *
kolor=['red', 'orange', 'green', 'blue']
speed('fastest')
tracer(0,0)

def slup(a, b, kol):
    fillcolor(kol)
    begin_fill()
    fd(a)
    rt(90)
    fd(b)
    rt(90)
    fd(a)
    rt(90)
    fd(b)
    end_fill()

def rysunek(a,b):
    pu()
    fd(100)
    pd()
    fillcolor('yellow')
    begin_fill()
    rt(90)
    for i in range(a):
        fd(b)
        rt((360/a))
    end_fill()
    lt(90)
    for i in range(a):
        kol = kolor[i%4]
        slup(b+(b/2)*i, b, kol)
        pu()
        fd(-b)
        rt(90+(360/a))
        pd()
    input()

rysunek(40,15)
