n = int(input('podaj srednice kola: '))

l=4

def kolo(n,l):
    r=n/2
    o=n//2
    for k in range(n):
        print(l*" ",end="")
        for j in range(n):
            if (k-o)**2+(j-o)**2 <= r**2:
                print("#",end="")
            else:
                print(" ",end="")
        print()

kolo(n,l)
kolo(n+2,l-1)
kolo(n+8,l-4)