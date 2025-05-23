slowa = open('lista7/popularne_slowa.txt', encoding="utf-8").read().split()
awols = slowa
slowa = set(slowa)
for i in range(len(awols)):
    awols[i] = awols[i][::-1]
awols = set(awols)
wynik = (slowa & awols)
print(wynik)
