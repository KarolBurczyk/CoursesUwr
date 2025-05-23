def potega(n, m):
    suma=1
    if n>m:
        return 1
    maks = 1
    maks_licz = 0
    i=0
    while i!=1:
        p = n
        i = 1
        while maks*p*p<m:
            if maks*p*p < m:
                p = p * p 
                i=i+i
            else:
                maks_licz+=i
                maks*=p
                
    
    return maks_licz

print(potega(2,33))
    
    

    