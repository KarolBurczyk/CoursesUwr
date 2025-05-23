def fun(r1, r2, n):
    i = 0
    a=1
    b = ['']*n
    while i!=n-1:
        if b[i]=='':
            b[i]=1
            i=r1[i]
            print(b)
        elif b[i]==1:
            b[i]=2
            i=r2[i]
            print(b)
        else:
            a=0
            break
    if a==0:
        print('0')
    else:
        print('1')

    


r1 = [0,0,0,0,4]
r2 = [2,3,3,2,4]
fun(r1, r2, 5)

