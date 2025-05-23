import random

znaki = ['.', '?', '!']

def zredukuj(nowy_tekst, l_slow):
    if len(nowy_tekst) <= l_slow:
        return " ".join(nowy_tekst)
    else:
        for i in range(len(nowy_tekst) - l_slow):
            del nowy_tekst[random.randint(0, len(nowy_tekst) - 1)]
        res = " ".join(nowy_tekst)
        if '.' not in nowy_tekst: # jeżeli ostatni wyraz nie kończy się kropką, to w tym momencie go oddajemy
            res += '.'
            return res
        return res 


def uprosc_zdanie(tekst, dl, l_slow):
    tekst = tekst.split()
    nowy_tekst = []
    for elem in tekst:
        if len(elem) <= dl:
            nowy_tekst.append(elem)
        elif '.' in elem: 
            if len(elem) <= dl + 1:
                nowy_tekst.append(elem)
    return zredukuj(nowy_tekst, l_slow)

def uprosc_tekst(tekst, dl, l_slow):
    with open(tekst) as f:
        t = f.read()
    t = t.split(' ')
    res = ""
    zdanie = ""
    i = 0
    while i < len(t):
        if t[i][len(t[i]) - 1] in znaki:
            zdanie += t[i]
            zdanie += ' '
            res += uprosc_zdanie(zdanie, dl, l_slow)
            res += ' '
            zdanie = ' '
            i += 1
        else:
            zdanie += t[i]
            zdanie += ' '
            i += 1
    return res
            



    
# print(uprosc_zdanie("Podział peryklinalny inicjałów wrzecionowatych \
# kambium charakteryzuje się ścianą podziałową inicjowaną \
# w płaszczyźnie maksymalnej.", 10, 5))

print(uprosc_tekst("tekst.txt", 10, 5))
