######################################
#  kostki.py
######################################

import random

def kostka():
    return random.randint(1,6)
    
while True:
    k1 = kostka()
    k2 = kostka()
    print (k1, k2, sep=',', end=' ')
    if k1 == 6 and k2 == 6:
        break    
print()     

   
######################################
#  rev.py
######################################

# zadanie: odwróć listę, tzn. zamień np. [3,4,5] na [5,4,3]
import time

def rev1(L):
    return list(reversed(L))
    
def rev2(L):
    L = L[:]
    for i in range(len(L) // 2):
        L[i], L[len(L)-i-1] = L[len(L)-i-1], L[i]
    return L   

def rev2b(L):
    L = L[:]
    for i in range(len(L) // 2):
        L[i], L[-i-1] = L[-i-1], L[i]
    return L   

def rev3(L):
    return L[::-1]
    
def rev4(L):
    wynik = []
    for i in range(len(L)):
        wynik.append(L[-i-1])
    return wynik
    
def rev4b(L):
    wynik = []
    for i in range(len(L)-1, -1, -1):
        wynik.append(L[i])
    return wynik  
    
def rev5(L):
    wynik = []
    for e in L:
        wynik.insert(0, e)
    return wynik               

N = 500000
def test(rev):
    L = list(range(N))
    t0 = time.time()
    rev(L)
    return time.time() - t0
    
for f in [rev1, rev2, rev3, rev4, rev5]:
    print (f, test(f))
    

