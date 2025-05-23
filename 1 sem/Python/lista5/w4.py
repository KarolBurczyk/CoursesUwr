######################################
#  gradient.py
######################################

# Gradient -- przejście z jednego koloru do drugiego

import random
from turtle import *
import numpy as np

def move(x, y):
    penup()
    goto(x,y)
    pendown()

def kwadrat(x, y, bok, kolor):
    move(x, y)
    begin_fill()
    fillcolor(kolor)
    for i in range(4):
        fd(bok)
        rt(90)
    end_fill()   
  
speed('fastest')    

kolor1 = np.array([1,1,0.5])
kolor2 = np.array([0.1, 0.1, 1])

N = 20
BOK = 50

for i in range(N+1):
    alfa = i / N
    mieszanka = (1-alfa) * kolor1 + alfa * kolor2
    kwadrat(-200 + BOK * i,0,  BOK, mieszanka)

input()


######################################
#  koch.py
######################################

from turtle import *

speed('fastest')

def koch(poziom, dlugosc):
    if poziom == 0:
        fd(dlugosc)
    else:
        dlugosc_nowa = dlugosc / 3
        koch(poziom -1, dlugosc_nowa)
        lt(60)
        koch(poziom -1, dlugosc_nowa)
        rt(120)
        koch(poziom -1, dlugosc_nowa)
        lt(60)
        koch(poziom -1, dlugosc_nowa)
        
for i in range(3):
    koch(4, 300)
    rt(120)        

input()


######################################
#  operacje_na_plikach.py
######################################


plik = open('popularne_slowa.txt', 'r')  # 'r' -- czytanie, można pominąć, 'rb' -- czytanie binarnego

tekst = plik.read().split()
#wiersze_pliku = plik.readlines() # alternatywa

print (tekst[:10])
print (wiersze_pliku[:10])


for wiersz in open('popularne_slowa.txt'):   # najlepszy sposób przetwarzania pliku tekstowego
#for wiersz in open('popularne_slowa.txt').readlines():
    wiersz = wiersz.rstrip() # usuń białe znaki z końca
    if 'kura' in wiersz:
        print (wiersz)
        
        
        
######################################
#  podwojne_slowa.py
######################################

# szukamy słów, która składają się z dwóch innych słów: kura-tor, wał-koń, ...

slowa = set(open('popularne_slowa.txt').read().split())

for w in slowa:
    for p in range(4, len(w) - 4):
        a = w[:p]
        b = w[p:]
        if a in slowa and b in slowa:
            print (a + '-' + b)
    
    

######################################

#  usun_duplikaty.py
######################################

# cel: usun_duplikaty([1,4,2,3,1,2,6,7,7,7]) -> [1,4,2,3,6,7] 

def usun_duplikaty1(L): # wolna wersja
    wynik = []
    for e in L:
        if e not in wynik:
            wynik.append(e)
    return wynik
    
def usun_duplikaty2(L): # wolna wersja
    wynik = []
    zbior = set()
    
    for e in L:
        if e not in zbior:
            wynik.append(e)
            zbior.add(e)
    return wynik
    
    
print (usun_duplikaty2([1,2,4,3,1,2,6,7,7,7]))

N = 7
nowy = usun_duplikaty2( list(range(10 ** N)))
print (len(nowy))


######################################
#  zbiory.py
# (nagranie sesji interaktywnej)
######################################

a = {1,2,3}
b = {3,4,5}
{1,2,3} == {3,2,1}
{1,2,3} == {3,2,1,1,1,1,3,3,3,3,2}
list(a)  # przekształcenie na listę
a.add(10) # dodanie elementu
a
a | b  # suma zbiorów
a & b  # czść wspólna zbiorów
a | {1000}
a - b
a
b
3 in a  # należenie do zbioru (szybkie!)
33 in a
33 not in a
not (33 in a)
a & b
a == b
a <= b  # zawieranie zbiorów
b <= a
a,b
len(a)  # liczba elementów w zbiorze
len({1,2,3,4,4,4,4,4})

L = [1,2,2,2,2,3,3,3,4,1,1,1]
len(set(L)) # liczba unikalnych elementów w liście

for element in a:  # 'jakaś' kolejność
    print (element)
    
for element in sorted(a): # iteracja po posortowanych elementach
    print (element)

sorted(L) # nie zmienia listy L
L
L.sort()  # zmienia
L
L.append(0)
L
x=L.sort()
L
x
print(x)
%history -f zbiory.py # zapisanie sesji do pliku
