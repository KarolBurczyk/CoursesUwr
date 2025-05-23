import random

arabia = ['Arabia_Saudyjska', 2, 3, 0.3, 0.3]
argentyna = ['Argentyna', 4, 6, 0.5, 0.8]
meksyk = ['Meksyk', 3, 4, 0.6, 0.5]
polska = ['Polska', 2, 3, 0.9, 0.8]

# druzyna = nazwa, obrona, ofensywa, bramkarz, bramkostrzelnosc

def mecz(A, B):
    oA = A[2]+random.randint(1,6)
    oB = B[2]+random.randint(1,6)
    dA = A[1]+random.randint(1,6)
    dB = B[1]+random.randint(1,6)
    if oA>dB:
        goleA = 0
        for i in range(oA-dB):
            if random.random()*A[4]>random.random()*B[3]:
                goleA+=1
    else:
        goleA = 0
    if oB>dA:
        goleB = 0
        for i in range(oB-dA):
            if random.random()*B[4]>random.random()*A[3]:
                goleB+=1
    else:
        goleB = 0
    a = [A[0], goleA, ':', goleB, B[0]]
    return a

def prawdopodobienstwo():
    pol = 0 
    arg = 0
    for i in range(100000):
        a = mecz(polska, argentyna)
        if a[1]>a[3]:
            pol+=1
        else:
            arg+=1
    return pol/arg

grupa = [arabia, argentyna, meksyk, polska]

def rozgrywki_grupowe(lista_drużyn, czy_wypisywać_wyniki):
    t = []
    for i in range(len(lista_drużyn)):
        t.append([lista_drużyn[i], 0, 0])
    for i in range(len(lista_drużyn)-1):
        for j in range(i+1, len(lista_drużyn)):
            a = mecz(lista_drużyn[i], lista_drużyn[j])
            if czy_wypisywać_wyniki==1:
                print(a[0], a[1], a[2], a[3], a[4])
            if a[1]>a[3]:
                t[i][1]+=3
                t[i][2]+=(a[1]-a[3])
                t[j][2]+=(a[3]-a[1])
            elif a[1]==a[3]:
                t[i][1]+=1
                t[j][1]+=1
            else:
                t[j][1]+=3
                t[j][2]+=(a[3]-a[1])
                t[i][2]+=(a[1]-a[3])
    for i in range(len(lista_drużyn)-1):
        for j in range(i+1, len(lista_drużyn)):
            if t[i][1]<t[j][1]:
                t[i], t[j] = t[j], t[i]
            elif t[i][1]==t[j][1]:
                if t[i][2]<t[j][2]:
                    t[i], t[j] = t[j], t[i]
                elif t[i][2]==t[j][2] and random.randint(0,1)==1:
                    t[i], t[j] = t[j], t[i]
    print()
    print('TABELA: ')
    for i in range(len(lista_drużyn)):
        print(t[i][0][0], 'punkty:', t[i][1], 'bilans:', t[i][2])

def rozgrywki_grupowe_ret(lista_drużyn):
    t = []
    for i in range(len(lista_drużyn)):
        t.append([lista_drużyn[i], 0, 0])
    for i in range(len(lista_drużyn)-1):
        for j in range(i+1, len(lista_drużyn)):
            a = mecz(lista_drużyn[i], lista_drużyn[j])
            if a[1]>a[3]:
                t[i][1]+=3
                t[i][2]+=(a[1]-a[3])
                t[j][2]+=(a[3]-a[1])
            elif a[1]==a[3]:
                t[i][1]+=1
                t[j][1]+=1
            else:
                t[j][1]+=3
                t[j][2]+=(a[3]-a[1])
                t[i][2]+=(a[1]-a[3])
    for i in range(len(lista_drużyn)-1):
        for j in range(i+1, len(lista_drużyn)):
            if t[i][1]<t[j][1]:
                t[i], t[j] = t[j], t[i]
            elif t[i][1]==t[j][1]:
                if t[i][2]<t[j][2]:
                    t[i], t[j] = t[j], t[i]
                elif t[i][2]==t[j][2] and random.randint(0,1)==1:
                    t[i], t[j] = t[j], t[i]
    return [t[0][0], t[1][0]]


def ppd():
    pol=0
    inni=0
    for i in range(10000):
        if rozgrywki_grupowe_ret(grupa)[0][0]=='Polska' or rozgrywki_grupowe_ret(grupa)[1][0]=='Polska':
            pol+=1
        else:
            inni+=1
    return pol/inni

#print(mecz(polska, arabia))
#print(prawdopodobienstwo())
#rozgrywki_grupowe(grupa, 1)
print('Prawdopodobienstwo wyjscia z grupy:', ppd())

