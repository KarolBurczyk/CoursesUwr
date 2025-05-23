L=[1,2,3,1,2,3,8,2,2,2,9,9,4]


def usun_duplikaty(L):
    L1 = []
    for i in range(len(L)):
        L1.append((L[i],i))
    L1.sort()
    wynik=[L1[0]]
    for i in range(1,len(L1)):
        if L1[i][0]>L1[i-1][0]:
            wynik.append(L1[i])
    wynik.sort(key=lambda tup: tup[1])
    for i in range(len(wynik)):
        print(wynik[i][0], end=' ')
usun_duplikaty(L)