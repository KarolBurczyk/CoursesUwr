def funkcja(a, k, n):
    b=['']*n
    licznik = 0
    for i in range(n):
        x=a[i]%10
        info=True
        for j in range(n):
            if x==b[j]:
                info = False
                j=n
        if info!=False:
            b[licznik]=x
            licznik+=1
        if licznik==k:
            return i
    return 0

a = [5, 15, 25, 35, 7, 8, 9]
print(funkcja(a, 2, 7))