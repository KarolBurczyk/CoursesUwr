from turtle import *
speed('fastest')

goto(-200,-150)
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

l=0
for i in range(15):
    for j in range(15):
        pu()
        goto(-195+i*30, -125+j*30)
        pd()
        if l%2==0:
            fillcolor('white')
        else:
            fillcolor('black')
        begin_fill()
        for k in range(4):
            fd(20)
            lt(90)
        end_fill()
        l+=1
input()