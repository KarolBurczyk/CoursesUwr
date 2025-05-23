slowa = open('lista7/popularne_slowa.txt', encoding="utf-8").read().split()
lalka = open('lista7/Bolesław Prus.txt', encoding="utf-8").read().split()
slowa = set(slowa)

for i in range(len(lalka)-50):
    for k in range(5):
        a=''
        for j in range(i,5+i+k):
            a=a+lalka[j][0]
        if a.lower() in slowa:
           print(a.lower(), lalka[i:i+5+k])
