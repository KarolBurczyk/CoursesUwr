a = [1,2,3,4,5,4,6,3,6,4,2]

def Program(x, a):
    n=len(a)-1
    i=0 
    res=0
    while i!=n: 
        if a[i]==x:
            res=res+1
        i=i+1
    return res

print(Program(4,a))

#niezmiennik: {i=0} while i!=n: {i=n}

#zadanie 2:
'''
int poti(int a, int b)
{   
    int n=a, k=b, res = 1;
    while (k!=0) {
    if (k%2!=0) {
        res = res * n;
        k = k - 1;
    }
    else {
        n = n * n;
        k = k / 2;
    }
    }
   return res;
}
'''

'''
{k=b}
while k!=0:
    if k%2!=0:
        k = k - 1
    else:
        k = k / 2
{k=0}
'''
#zadanie 4
"""
a)
z każdym obejściem pętli k jest albo dzielone przez dwa(jeżeli jest podzielne) albo pomniejszane o 1
a więc po iluś obejściach dojdziemy do k=1 i w następnym obejściu k=0, co nie spełnia warunku pętli while, więc ją opuszczamy 
i algorytm się kończy

b)

"""