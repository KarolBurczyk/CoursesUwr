lalka = open('Python\lista8\Bolesław Prus.txt', encoding="utf-8").read().split()
popularne = open('Python\lista8\popularne_slowa.txt', encoding="utf-8").read().split()
popularne = set(popularne)

polskie_znaki = ['ą', 'ę', 'ć', 'ż', 'ź', 'ó', 'ł', 'ń', 'ś']
polskie_znaki = set(polskie_znaki)

znaki = ['.', ',', '!', '-', '(', ')', '[', ']', '?', '„', '”', '*', ':', ';', '/']
znaki = set(znaki)

maks = ''
maks_id = len(maks)
liczba = 0
start = 0

for i in range(len(lalka)):
    if lalka[i].lower() in popularne:
        for j in range(len(lalka[i])):
            if lalka[i][j].lower() in polskie_znaki:
                if liczba > maks_id:
                    maks = lalka[start:i]
                    maks_id = liczba
                liczba = 0
                start = i + 1
                break
            elif lalka[i][j] not in znaki:
                liczba+=1
    else:
        if liczba > maks_id:
            maks = lalka[start:i]
            maks_id = liczba
        liczba = 0
        start = i + 1

for i in range(len(maks)):
    print(maks[i], end=' ')
