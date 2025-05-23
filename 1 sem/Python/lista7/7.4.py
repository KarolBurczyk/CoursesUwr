def podziel(s):
    i = 0
    wynik = []
    while i<len(s)-1:
        k = i
        if s[i]!=' ' and i<len(s)-1:
            while s[i]!=' ' and i<len(s)-1:
                i+=1
            wynik.append(s[k:i])
        i+=1
    return wynik



print(podziel('Ala   sushi  k  loooool         ma    kota!'))