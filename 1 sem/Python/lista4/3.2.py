import math

def czypierwsza(a):
    c = int(math.sqrt(a)) + 1
    for i in range(2,c):
        if a%i==0:
            return 0
    return 1

s='7777777'
n=10 #ilosc cyfr
n=n-7
m=0
l=0
lista=['']

while n>=0:
    if n>0:
        for i in range(1,10**n):
            k = s + (n-len(str(i))) * '0' + str(i)
            if m>0:
                for j in range(10**(m-1),10**m):
                    h = str(j) + k
                    if czypierwsza(int(h))==1:
                        lista.append(h)
                        print(h)
                        l+=1
            else:
                if czypierwsza(int(k))==1:
                    lista.append(k)
                    print(k)
                    l+=1
    else:
        for p in range(10**(m-1),10**m):   
            h = str(p) + s
            if czypierwsza(int(h))==1:
                lista.append(h)
                print(h)
                l+=1
    n-=1
    m+=1

#print(set(lista))
print(len(set(lista))-1)

