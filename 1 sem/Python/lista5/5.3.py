import random

from numpy import longlong 
n = int(input('podaj n: '))

lista = []

def randperm(n):
    for i in range(n+1):
        lista.append(i)

    perm = []
    while n>=0:
        k = random.randint(0,n)
        perm.append(lista[k])
        lista[k]=lista[n]
        n-=1
    return perm

s=randperm(n)
print('gotowe')