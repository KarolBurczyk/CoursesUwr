
def kompresja(tekst):
    tekst = tekst.split()
    zdanie = []
    for slowo in tekst:
        indeks = 1
        tmp = [(slowo[0], 1)]
        while indeks < len(slowo):
            if slowo[indeks] == tmp[len(tmp) - 1][0]:
                tmp[len(tmp) - 1] = (tmp[len(tmp) - 1][0], tmp[len(tmp) - 1][1] + 1)
                indeks += 1
            else:
                tmp.append((slowo[indeks], 1))
                indeks += 1
        zdanie.append(tmp)
    return zdanie

def zloz_slowo(tekst):
    res = ""
    for elem in tekst:
        res += elem[1] * elem[0]
    return res

def dekompresja(tekst):
    res = ""
    for elem in tekst:
        res += zloz_slowo(elem)
        res += " "
    return res

print(dekompresja(kompresja("baaardzo dlugiiii proograammmm")))
with open("tekst.txt") as f:
    t = f.read()
print(kompresja(t))