from turtle import *
import random

colors = {
   'r' : 'red', 
   'g' : 'green', 
   'b' : 'blue',
   'y' : 'yellow',
   'o' : 'orange', 
}

dor = ['bobby' + 'bobby'+ 'bobby', 'rybogryby', 'grrrrrry', 'yo' * 10] * 2

speed('fastest')
lt(90)

def kwadrat(kolor):
    fillcolor(kolor)
    begin_fill()
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    fd(30)
    lt(90)
    end_fill()

def kolko():
    tracer(0,0)
    kat=360/len(dor)
    for j in range(len(dor)):
        pu()
        fd(200)
        pd()
        kacik=360/len(dor[j])
        for i in range(len(dor[j])):
            pu()
            fd(30)
            pd()
            kwadrat(colors[dor[j][i]])
            pu()
            fd(-30)
            lt(kacik)
            pd()
        pu()
        fd(-200)
        lt(kat)
        pd()
    input()

kolko()
        
