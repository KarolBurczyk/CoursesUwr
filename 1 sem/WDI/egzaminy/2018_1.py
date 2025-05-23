def funkcja(n, x):
    array = ['']*n
    k = n//2
    tmp = 0 
    for i in range(n//2):
        while x[k]<x[i] and k<n:
            k+=1
            if k>=n:
                break
        array[i] = k-(n//2)+i-tmp
        if x[i]!=x[i+1]:
            tmp = 0
        else:
            tmp+=1
    k = 0
    tmp = 0
    for i in range(n//2, n):
        while x[k]<x[i] and k<(n//2):
            k+=1
        array[i] = k+(i-n//2)-tmp
        if i<n-1:
            if x[i]!=x[i+1]:
                tmp = 0
            else:
                tmp+=1
    print(array)



x = [(-1), 5, 6, 4,4,4]
funkcja(6,x)

#idea: przechodzę po kolei po elementach od x[0] do x[n/2-1] i sprawdzam ile elementow z przedzialu od x[n/2] do x[n-1] jest wiekszych
#jednoczesnie nie cofajac sie caly czas do x[n/2] a doliczajac do poprzeniej liczby pamietajac o tym, ze sa posortowane i doliczajac liczbe
#liczbe elementow w ciagu przez ktora juz przeszedlem, druga strona nastepuje analogicznie

#zlozonosc O(n)