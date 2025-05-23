def czypalindrom(n,k):
    t = []
    while n>0:
        t.append(n%k)
        n//=k
    for i in range(len(t)//2+1):
        if t[i]!=t[len(t)-1-i]:
            return 0
    return 1
    
print(czypalindrom(45,2))

#zlozonosc o(2log(k(n))