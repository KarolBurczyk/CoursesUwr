n = int(input('podaj n: '))
m = int(input('podaj m: '))

def ilecyfr(n):
    t = [0] * 10
    while n>0:
        t[n%10]+=1
        n=n//10
    p=0
    for i in range(10):
        if t[i]>0:
            p+=1
    return t

if ilecyfr(n)==ilecyfr(m):
    print('sa podobne')
else:
    print('nie sa podobne')
