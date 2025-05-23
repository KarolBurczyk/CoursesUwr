n = int(input('podaj n:'))
m = int(input('podaj m:'))

t = [1]*(n+3)

for i in range(2,n+1):
    if t[i]==1:
        if i<m and m%i==0:
            for j in range(m+m%i, n+1, i):
                t[j]=0
        elif i<m:
            for j in range(m+(i-m%i), n+1, i):
                t[j]=0 
    else:
        for j in range(i+i, n+1, i):
            t[j]=0

for i in range(m, n+1):
    print(i, t[i])   
