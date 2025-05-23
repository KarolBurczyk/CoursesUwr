'''
a) 
    1)  2
    2)  2
    3)  3
    4)  4
    5)  10
    6)  5
b)
    ilosc czynnikow przy rozlozeniu liczby n na czynniki pierwsze
c) ::
'''
def ilosc_dzielnikow(n):
    licznik = 0 
    for i in range(2,n//2+1):
        if n%i==0:
            licznik +=1
            while n%i==0:
                n = n/i
        if n==1:
            return licznik

print(ilosc_dzielnikow(90))
        

