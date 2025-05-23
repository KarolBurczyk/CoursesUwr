k = int(input('podaj liczbe: '))
l = int(input('podaj liczbe: '))

def nwd(a,b):
    while a!=b:
        if b>a:
            a,b = b,a
        a = a - b
    return a

print((k*l)/nwd(k,l))