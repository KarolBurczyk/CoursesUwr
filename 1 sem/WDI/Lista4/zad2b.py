a = int(input('podaj licznik: '))
b = int(input('podaj mianownik: '))

if b>a:
    for i in range(2,a+1):
        while b%i==0 and a%i==0:
            a=a/i
            b=b/i
else:
    for i in range(2,b+1):
        while b%i==0 and a%i==0:
            a=a/i
            b=b/i
print(int(a),'/',int(b))

