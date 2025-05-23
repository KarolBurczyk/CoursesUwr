'''def gcd(n,m):
    if (m==0): 
        return n
    if (n<m): 
        return gcd(m,n)
    ilenp = n%2 + m%2
    if (ilenp==2):
        return gcd(n-m,m)
    if (ilenp==0):
        return 2*gcd(n/2,m/2)
    if (n%2==0): 
        return gcd(n/2,m)
    else: 
        return gcd(n,m/2)'''

def gcd1(n,m):
    i = 1
    while m!=0:
        if (n<m): 
            n, m = m, n
        ilenp = n%2 + m%2
        if (ilenp==2):
            n = n - m
        elif (ilenp==0):
            n = n/2
            m = m/2
            i = i * 2
        elif (n%2==0): 
            n = n/2
        else: 
            m = m/2
    return n*i

#print(gcd(81,18))
print(gcd1(81,18))