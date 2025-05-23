def potega(n, m):
    suma=1
    if n>m:
        return 1
    p = n
    i = 1
    while p<m:
        p = p * n 
        i=i+1
    return i

print(potega(2,33))
    
    

    