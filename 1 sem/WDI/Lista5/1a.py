k = int(input('podaj k: '))

def pot(a, b):
    rez = 1
    i = 0
    s = []
    while b>0:
        if b%2:
            rez = rez * a
            i+=1
        b = b // 2
        s.append(a)
        a = a * a
    return [i, s]

res1 = pot(2,k)
res2 = pot(2,k+1)
if res1[0]>res2[0]:
    print('b:', k, 'ilosc mnozen:', res1[0], 'kolejne potegi a:', res1[1])
elif res1[0]<res2[0]:
    print('b:', k+1, 'ilosc mnozen:', res2[0], 'kolejne potegi a:', res2[1])
else:
    print('idencztyczna liczba mnozen')