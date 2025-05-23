s = input('podaj slowo:')
x = input('podaj drugie slowo:')

def slowa(s, x):
    slownik = {
        s[0]: 1
    }

    for i in range(1, len(s)):
        if s[i] not in slownik:
            slownik[s[i]] = 1
        else:
            slownik[s[i]] +=1

    for i in range(len(x)):
        if x[i] in slownik and slownik[x[i]]>0:
            slownik[x[i]] = slownik[x[i]] - 1
        else:
            return 'nie zawiera sie'
    return 'zawiera sie'
    


print(slowa(s, x))