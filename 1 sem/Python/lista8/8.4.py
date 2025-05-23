from turtle import *

kolory = {
  "R": "red",
  "G": "green",
  "Y": "yellow",
  "B": "blue"
}

kolorki = {
  0: "R",
  1: "G",
  2: "Y",
  3: "B"
}

def kwadrat(bok, kolor):
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
      fd(bok)
      rt(90)
    end_fill()
    
def murek(s,bok):
  kolor = "black"
  for a in s:
     if a == 'f':
         kwadrat(bok, kolor)
         fd(bok)
     elif a == 'b':
         kwadrat(bok, kolor)
         fd(bok)         
     elif a == 'l':
         bk(bok)
         lt(90)
     elif a == 'r':
        rt(90)
        fd(bok)
     elif a == 'G' or a == 'B' or a == 'R' or a == 'Y':
        kolor = kolory[a]

def spirala(n):
    while n>=0:
        murek(kolorki[n%4]+n*'f'+'l',10)  
        n=n-1
        
ht()

tracer(0,0) # szybkie rysowanie     
spirala(10)
update() # uaktualnienie rysunku

input()
