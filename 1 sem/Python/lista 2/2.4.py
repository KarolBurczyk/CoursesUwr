from duze_cyfry import daj_cyfre

k = int(input('podaj liczbe : '))
s=[]
while k>0:
    s.append(k%10)
    k//=10

int(s[len(s)-1]) 
l=len(s)-1

for i in range(5):
    for j in range(l+1):
        print (daj_cyfre(int(s[l-j]))[i]," ",end="")
    print("")
