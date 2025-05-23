def wstaw(L, e):
    for i in range(len(L)):
        if e<L[i]:
            return L[:i] + [e] + L[i:]
    return L + [e]

def posortowana(L, klucz):
    wynik = []
    for e in L:
        wynik = wstaw(wynik, e)
    return wynik

lista = [6,7,8,9,1,2,3,4,5]
print(posortowana(lista, len))