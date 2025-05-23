n = int(input('podaj n:'))

t = []

a = 1
i = 1
while a*i<=n:
    i+=1
    a*=i
a=a/i
i=i-1
t.append(i)
n = n - a*i
while i!=1:
    a = a / i
    i = i - 1
    if n-a*i>=0:
        t.append(i)
        n = n - a*i
    else:
        t.append(0)

print(t)
