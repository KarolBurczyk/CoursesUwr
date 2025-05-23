import random


def kostka():
    return random.randint(1,6)

while True:
    a = kostka()
    b = kostka()
    print (a , b, sep='|', end=' ')
    if a == 6 and b == 6:
        break
#losujemy dopoki nie wypadna 2 * 6