a = [1, 2, 3, 5, 6]

def wstawianie(a, x):
    lewy=0
    prawy=len(a)-1
    while lewy<prawy:
        k=(lewy+prawy)//2
        if a[k]<x:
            lewy=k
        else:
            prawy=k
    a.insert(x)