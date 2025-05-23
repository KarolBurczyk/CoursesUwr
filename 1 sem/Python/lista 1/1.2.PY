a = 2 * 3 * 4
print (4, ' ma ', len(str(a)), 'cyfry')
for i in range (5,101):
    a = a * i
    if len(str(a)) % 100 == 12 or len(str(a)) % 100 == 13 or len(str(a)) % 100 == 14:
        print (i, ' ma ', len(str(a)), 'cyfr' )
    elif len(str(a)) % 10 > 1 and len(str(a)) % 10 < 5:
        print (i, ' ma ', len(str(a)), 'cyfry' )
    else: 
        print (i, ' ma ', len(str(a)), 'cyfr' )
    #możemy liczyć liczbę cyfr również przez wykonanie pętli dzielącej przez 10 do momentu uzyskania zera i zliczając jej obejścia
