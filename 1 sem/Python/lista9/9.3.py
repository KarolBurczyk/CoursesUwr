plik = open('Python\lista9\popularne_slowa.txt', encoding='utf-8').read().split()

def slowa(slownik, x):
    for i in range(len(x)):
        if x[i] in slownik and slownik[x[i]]>0:
            slownik[x[i]] = slownik[x[i]] - 1
        else:
            return 0
    return 1

def funkcja(s):
    slownik = {
        s[0]: 1
    }
    for i in range(1, len(s)):
        if s[i] not in slownik:
            slownik[s[i]] = 1
        else:
            slownik[s[i]] +=1

    for i in range(len(plik)-1):
        #for j in range(len(plik)-1):
            if slowa(slownik, plik[i])==1:
                print(plik[i])

funkcja('bolesław prus')