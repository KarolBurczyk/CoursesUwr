######################################
#  anonimizacja.py
######################################

import random

# Cel: "Ala ma 3 koty i 27 kanarków" -> "Ala ma * koty i ** kanarków"

def safe_int(d):
    try:
        return int(d)
    except ValueError:
        return None

def jest_cyfra(d): 
    return ord(d) >= 48 and ord(d) <= 57
    
def jest_cyfra(d):
    return d in '0123456789'
    
def jest_cyfra(d):
    return safe_int(d) in range(10)
    
def jest_cyfra(d):
    return d.isdigit()
    
def jest_cyfra(d):
    return '0' <= d <= '9'
    
def jest_cyfra(d):
    return safe_int(d) in [0,1,2,3,4,5,6,7,8,9]

     
    
def usun_cyfry1(napis):
    wynik = ''
    for a in napis:
        if jest_cyfra(a):
            wynik += '*'  # wynik = wynik + '*'
        else:
            wynik += a
    return wynik
    
def usun_cyfry2(napis):
    wynik = []
    for a in napis:
        if jest_cyfra(a):
            wynik.append('*')
        else:
            wynik.append(a)
    return ''.join(wynik)
    
    
    
print (usun_cyfry2("Ala ma 3 koty i 27 kanarków"))      
    
######################################
#  tablica2d.py
######################################

import random

def wybierz_znak(s):
    return s[random.randint(0, len(s)-1)]

def pisz(t):
    for wiersz in t:
        print (''.join(wiersz))
    
znaki = 'abcdeefghijk'

N = 7
M = 200

#tab = N *[N * ['.']]    # błędna konstrukcja, wiersze są zunifokowane

tab = [ N * ['.'] for i in range(N)]

for i in range(M):
    y = random.randint(0, N-1)
    x = random.randint(0, N-1)
    tab[y][x] = wybierz_znak(znaki)
    
pisz(tab)    

    
    


######################################
#  losowe_spacery.py
######################################


from turtle import pensize, pencolor, fd, bk, rt, lt, speed
import random

pensize(4)
speed('fastest')

N = 300
D = 10
R = 55

kolory = [ 'orange', 'red', 'green', 'lightgreen', 'cyan', 'blue', 'yellow' ]

for i in range(N):
    kolor = random.choice(kolory)
    pencolor(kolor)
    fd(D)
    rt(random.randint(-R, R))
    
input('Koniec rysowania')    
    

######################################
#  rozeta.py
######################################

from turtle import *  # można tak, ale ostrożnie!
import random

speed('fastest')
pensize(2)

def kwadrat(bok):
    for i in range(4):
        fd(bok)
        rt(90)

def rozeta(a, b, n):
    for i in range(n):
        fd(a)
        kwadrat(b)
        bk(a)       # fd(-a)
        rt(360/n)
        
rozeta(100, 70, 18)
rozeta(50, 30, 36)

input()        
               
               
######################################
#  kwadrat1.py
######################################

# Rysujemy wiele kwadratów, nakładających się, o losowych kolorach
# Nowe funkcje: begin_fill, end_fill, fillcolor, goto
# Druga wersja: kwadraty rozdzielne, kolor obliczany

from turtle import *
import random

speed('fastest')

BOK = 30

def move(x, y):
    pu()
    goto(x, y)
    pd()

def kwadrat(x, y, bok, kolor):
    move(x, y)
    fillcolor(kolor)
    begin_fill()
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()
    
kolory = [ 'orange', 'red', 'green', 'lightgreen', 'cyan', 'blue', 'yellow' ]

for i in range(300):
    x = random.randint(0, 300)
    y = random.randint(0, 300)
    bok = random.randint(50, 150)
    kwadrat(x, y, bok, random.choice(kolory))
input()    
    

                

