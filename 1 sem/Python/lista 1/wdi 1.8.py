m = int(input('podaj m: '))
n = int(input('podaj n: '))

S = input("podaj slowo s: ")

T = input("podaj tekst t: ")

p=0

j=0
i=0

while j <  n-m+1:
    k=j
    while i < m:
        if S[i] == T[j]:
            j+=1
            i+=1
        else: 
            break
        if i==m:
            p+=1
    i=0
    j=k+1

print(p)

        



