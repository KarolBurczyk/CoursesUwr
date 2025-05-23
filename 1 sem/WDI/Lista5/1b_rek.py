k = int(input('podaj k: '))

def pot(a, b):
    if not b:
        return 1
    if b%2:
        s.append(a)
        s[0]+=1
        return a*pot(a*a,b//2)
    else:
        s.append(a)
        return pot(a*a,b/2)

s=[0]
pot(2,k)
res1=s
s=[0]
pot(2,k+1)
res2=s


if res1[0]<res2[0]:
    print('b:', k, 'ilosc mnozen:', res1[0], 'kolejne potegi a:', res1[1:])
elif res1[0]>res2[0]:
    print('b:', k+1, 'ilosc mnozen:', res2[0], 'kolejne potegi a:', res2[1:])
else:
    print('idencztyczna liczba mnozen')