'''
Karol Burczyk
lista 1: zadanie 2
PyCharm
'''


class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik


def uproszczenie(u):
    if u.licznik % u.mianownik == 0:
        return int(u.licznik / u.mianownik)
    for indeks in range(2, min(u.licznik, u.mianownik)+1):
        if u.licznik % indeks == 0 and u.mianownik % indeks == 0:
            u.licznik /= indeks
            u.mianownik /= indeks
    return int(u.licznik), int(u.mianownik)


def wartosc_ulamka(u):
    return u.licznik / u.mianownik


def operacje_nowy_element(u1, u2, znak):
    if znak == '*':
        return uproszczenie(Ulamek(u1.licznik * u2.licznik, u1.mianownik * u2.mianownik))
    elif znak == '/':
        return uproszczenie(Ulamek(u1.licznik * u2.mianownik, u1.mianownik * u2.licznik))
    elif znak == '+':
        return uproszczenie(Ulamek(u1.licznik * u2.mianownik + u1.mianownik * u2.licznik, u1.mianownik * u2.mianownik))
    elif znak == '-':
        return uproszczenie(Ulamek(u1.licznik * u2.mianownik - u1.mianownik * u2.licznik, u1.mianownik * u2.mianownik))


def operacje_drugi_argument(u1, u2, znak):
    if znak == '*':
        u2.mianownik *= u1.mianownik
        u2.licznik *= u1.licznik
        return uproszczenie(Ulamek(u2.licznik, u2.mianownik))
    elif znak == '/':
        u2.mianownik *= u1.licznik
        u2.licznik *= u1.mianownik
        return uproszczenie(Ulamek(u2.licznik, u2.mianownik))
    elif znak == '+':
        tmp = u2.mianownik
        u2.mianownik = u1.licznik * u2.mianownik + u1.mianownik * u2.licznik
        u2.licznik = u1.mianownik * tmp
        return uproszczenie(Ulamek(u2.licznik, u2.mianownik))
    elif znak == '+':
        tmp = u2.mianownik
        u2.mianownik = u1.licznik * u2.mianownik - u1.mianownik * u2.licznik
        u2.licznik = u1.mianownik * tmp
        return uproszczenie(Ulamek(u2.licznik, u2.mianownik))


print(operacje_drugi_argument(Ulamek(2, 7), Ulamek(2, 7), '*')) #przyklad
