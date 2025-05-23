from random import random


import random

def safe_int(d):
    try:
        return int(d)
    except ValueError:
        return None

def jest_cyfra(d):
    return ord(d) >= 48 and ord(d) <= 57 #ascii

def jest_cyfra(d):
    return d in '0123456789'

def jest_cyfra(d):
    return safe_int(d) in range(10)

def jest_cyfra(d):
    return safe_int(d) in [0 , 1, 2, 3, 4, 5, 6, 7, 8, 9]

def jest_cyfra(d):
    return d.isdigit()

def jest_cyfra(d):
    return '0' <= d <= '9'

def usun_cyfry(napis):
    wynik = ''
    for a in napis:
        if jest_cyfra(a):
            wynik += "*"
        else:
            wynik += a
    return wynik
    
def usun_cyfry2(napis):
    wynik = []
    for a in napis:
        if jest_cyfra(a):
            wynik.append("*")
        else:
            wynik.append(a)
    return ''.join(wynik)

print(usun_cyfry2('Ala ma 3 koty i 27 kanarkow'))