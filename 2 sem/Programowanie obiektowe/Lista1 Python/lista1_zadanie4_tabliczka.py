'''
Karol Burczyk
lista 1: zadanie 2
PyCharm
'''


import numpy as np

msc_po_przecinku = 2


def zaokraglenie(x):
    brakujace_cyfry = str(round(x, msc_po_przecinku))
    if len(brakujace_cyfry) == (msc_po_przecinku + 2):
        return str(round(x, msc_po_przecinku))
    else:
        return brakujace_cyfry + ((msc_po_przecinku + 2) - len(brakujace_cyfry)) * '0'


def tabliczka(x1, x2, y1, y2, skok):
    for x in np.arange(x1, x2 + skok, skok):
        for y in np.arange(y1, y2 + skok, skok):
            if x == x1 and y == y1:
                print(' ' * (msc_po_przecinku + 2), end=' ')
            elif x == x1:
                print(zaokraglenie(y - skok), end=' ')
            elif y == y1:
                print(zaokraglenie(x - skok), end=' ')
            else:
                print(zaokraglenie((y - skok) * (x - skok)), end=' ')
        print()


tabliczka(0.2, 1.3, 0.2, 3.14, 0.3) #przyklad
