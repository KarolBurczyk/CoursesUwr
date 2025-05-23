def czy_pierwsza(n):
    for i in range(2, int(n/2 + 1)):
        if n % i == 0:
            return False
    return True

def pierwsze_imperatywna(n):
    res = []
    if n <= 2:
        return "Nie ma takich liczb"
    for liczba in range(2, n):
        if czy_pierwsza(liczba):
            res.append(liczba)
    return res

def pierwsze_skladana(n):
    tmp = [i for i in range(2, n)]
    return [n for n in tmp if czy_pierwsza(n)]

def pierwsze_filtr(n):
    tmp = [i for i in range(2, n)]
    res = filter(czy_pierwsza, tmp)
    return list(res)

print(pierwsze_skladana(20))
print(pierwsze_imperatywna(20))
print(pierwsze_filtr(20))