a=[5,32,7,9,5,3,1]

def wstawianie(L):
    for i in range(1,len(L)):
        j=0
        while L[i]<L[len(L)-j-1] or (len(L)-j-1)!=0:
            j+=1
        L.insert(len(L)-j-1,L[i])
    return L

print(wstawianie(a))
