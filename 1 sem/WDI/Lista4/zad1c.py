n = int(input('podaj n: '))
x = int(input('podaj x: '))

s=0
p=x
for i in range(1,n+1):
    s=s+i*p
    p=p*x
print(s)

#zlozonosc o(n)