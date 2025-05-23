plik = open('costam.txt', 'r') #r - czytanie, rb - czytanie binarnego

tekst = plik.read().split()
wiersze_pliku = plik.readlines()

print (tekst[:10]) #wypisze w postaci ['slowo' , 'slowo2']
print (wiersze_pliku[:10]) #wypisze w postaci ['slowo/n' , 'slowo2/n']

for wiersz in open('costam.txt'): #- czyta prosto z tekstu i nie tworzy listy
#for wiersz in open('costam.txt').readlines(): - robi z tekstu liste tzn. zajmuje więcej pamięci i przy dużych plikach możę być problem
    wiersz = wiersz.rstrip() #usun biale znaki z konca (np: /n)
    if 'kura' in wiersz:
        print (wiersz)