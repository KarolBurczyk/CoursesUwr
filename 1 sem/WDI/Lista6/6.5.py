n = int(input('podaj n:'))

def pierwsze(n):
    t = []

    t = [1]*(n+3)

    for i in range(2,n+1):
        if t[i]==1:
            for j in range(i+i, n+1, i):
                t[j]=0
        if i*i>n:
            break

    for i in range(2, n+1):
        print(i, t[i])

pierwsze(n)
