n = int(input('podaj n: '))
k = int(input('podaj k: '))

t=[]
p=0
for i in range(k):
    liczba = int(input('podaj a:'))
    licznik = 0
    while n%liczba==0:
        licznik += 1
        n /= liczba
    if licznik>p:
        p = licznik
        t=[]
        t.append(liczba)
    elif licznik==p:
        t.append(liczba)
print(p, end=' ')
for i in range(len(t)):
    print(t[i], end=' ')

#zlozonosc o(k(p+1))