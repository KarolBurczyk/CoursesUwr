import random

#przypisywanie randomowych liter ze 'znaki' do randomowych pol w tablicy tab

def wybierz_znak(s):
    return s[random.randint(0, len(s) - 1)]

def pisz(t):
    for wiersz in t:
        print (''.join(wiersz))

znaki = 'abcdefghijkx'

n = 7
m = 200
#tab = n * [n * ['.']]

tab = [ n * ['.'] for i in range(n)]

for i in range(m):
    y = random.randint(0 , n-1)
    x = random.randint(0 , n-1)
    tab[y][x] = wybierz_znak(znaki)

pisz(tab)
# tab = (wykorzystać mnożenie!)