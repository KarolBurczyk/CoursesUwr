from losowanie_fragmentow import losuj_fragment

def losuj_haslo(n):
     haslo = ''
     while n != 0:
          s = losuj_fragment()
          if n-len(s) > 1:
               haslo = haslo + s
               n = n-len(s)
          elif n-len(s) == 0:
               haslo = haslo + s
               n = n-len(s)
     return haslo

n = int (input('Podaj n: '))

for i in range (10):
     print (i,': ', losuj_haslo(n))

     