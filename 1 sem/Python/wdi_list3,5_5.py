a = "1000" #str(input("podaj a"))
b = "0000" #str(input("podaj b"))
wynik = ""
amin = a[0] + (len(a)-1)*0
bmin = b[0] + (len(b)-1)*0
i=0
p=0
while len(a)-i-2>=0:
    l = int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + p
    print(int(a[len(a)-1-i]) , '+' , int(b[len(b)-1-i]) , '+' , p , '=' , l)
    if l==0:
        wynik = '0' + wynik
    elif l==1:
        wynik = '1' + wynik
    elif l>2:
        wynik = '1' + wynik
        p=1
    elif l==2:    
        wynik = '0' + wynik
        p=1
    i+=1
if p>0:
    wynik = '1' + wynik

while len(a)-i-2>=0:
    l = int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + p
    print(int(a[len(a)-1-i]) , '+' , int(b[len(b)-1-i]) , '+' , p , '=' , l)
    if l==0:
        wynik = '0' + wynik
    elif l==1:
        wynik = '1' + wynik
    elif l>2:
        wynik = '1' + wynik
        p=1
    elif l==2:    
        wynik = '0' + wynik
        p=1
    i+=1    

print(wynik)
