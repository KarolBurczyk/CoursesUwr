def czypalindrom(n):
    t = []
    while n>0:
        t.append(n%2)
        n//=2
    for i in range(len(t)//2+1):
        if t[i]!=t[len(t)-1-i]:
            return 0
    return 1

print(czypalindrom(45))