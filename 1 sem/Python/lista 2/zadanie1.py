def rev(S):
    for i in range(int(len(S))//2):
        S[i] , S[-i-1] = S[-i-1] , S[i] #zamiana
    return S

def rev1(S):
    wynik = []
    for i in range(len(S)):
        wynik.append(S[-i-1])
    return wynik

S=[1,2,3,4,5,6]
print(S)
print ('rev: ',rev(S)) 
print ('rev1:', rev1(S))
S.insert(0,7) #(pozycja,dane)
print (list(reversed(S)))
        