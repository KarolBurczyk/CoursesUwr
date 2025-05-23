#szukamy slowa, ltore sklada sie z 2 popularnych slow
#slowa = set(open('costam.txt').read().split())

'''for w in slowa:
    for p in range(4, len(w-4)):
        a = w[:p]
        b = w[p:]
        if a in slowa and b in slowa:
            print(a + '-' + b)'''

#tabele w pythonie to array[]
#2 wymiarowe to np a = tabela.array ( [[1, 2, 3], [1, 2, 3]] ) , a = tabela.array ( [[1, 2, 3], [1, 2, 3]] )
#a + b = ( [[2, 4, 6], [2, 4, 6]] )
np = np.zeros([4, 7])
print(np())
