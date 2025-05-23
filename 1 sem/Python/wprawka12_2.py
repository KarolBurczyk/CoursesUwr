from turtle import *
from math import sin
speed('fastest')

pu()
goto(-200,-150)
pd()
fillcolor('grey')
begin_fill()
for i in range(4):
    fd(15*30)
    lt(90)
end_fill()


for i in range(16):
    pu()
    goto(-200, -150+i*30)
    pd()
    fd(15*30)

rt(90)

for i in range(16):
    pu()
    goto(-200+i*30, -150)
    pd()
    fd(-15*30)

lt(90)

t = [15*[' '] for i in range(15)]



for i in range(15):
    for j in range(15):
        t[i][j] = round(sin(i+j), 3)
        pu()
        goto(-185+i*30, -135+j*30)
        fd(-abs(t[i][j])*15)
        rt(90)
        fd(abs(t[i][j])*15)
        lt(90)
        pd()
        if t[i][j]<0:
            fillcolor('black')
        else:
            fillcolor('white')
        begin_fill()
        for k in range(4):
            fd(abs(30*t[i][j]))
            lt(90)
        end_fill()
        #print(t[i][j], end=" ")
    #print()
input()
