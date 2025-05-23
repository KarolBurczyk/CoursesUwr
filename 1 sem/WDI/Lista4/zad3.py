n = int(input('podaj liczbe: '))

def nwd(a,b):
    while a!=b:
        if b>a:
            a,b = b,a
        a = a - b
    return a

a = int(input('podaj a: '))
b = int(input('podaj a: '))
a = nwd(a,b)

for i in range(n-2):
    b = int(input('podaj a: '))
    a = nwd(a,b)

print(a)

#zlozonosc o(n(a+b))