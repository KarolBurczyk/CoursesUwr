
def podliczenie(tab, mandaty):
    for i in range(mandaty):
        maks = 0 
        maks_id = 0
        for elem in tab:
            if elem[elem[1]] > maks:
                maks = elem[elem[1]]
                maks_id = tab.index(elem)
        tab[maks_id][1] += 1
        tab[maks_id][2] += 1
    for elem in tab:
        print(elem[0], elem[2])

def prog(komitety):
    suma = 0
    for elem in komitety:
        suma += elem[1]
    for elem in komitety:
        if elem[1]/suma <= 0.05:
            komitety.remove(elem)
    return komitety

def wybory(komitety, mandaty):
    hondt = []
    komitety = prog(komitety)
    for elem in komitety:
        tab = []
        tab.append(elem[0]) # 0 element nazwa komitetu
        tab.append(3) # 1 element to indeks ostatniego mandatu komitetu
        tab.append(0) # 2 element licznik mandatow
        for i in range(1, mandaty):
            tab.append(elem[1] / i) # 3 element : kolejne punktacje mandatow
        hondt.append(tab)
    podliczenie(hondt, mandaty)
        


wybory([("KO", 200), ("pis", 170), ("Lewica", 10), ("Konfa", 50)], 20)