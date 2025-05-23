n = int(input('podaj n: '))
s=0
for i in range(1,n+1):
    if i%2==0:
        s=s+1/i
    else:
        s=s-1/i
print(s)

#zlozonosc o(n)