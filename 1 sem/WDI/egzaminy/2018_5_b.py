def fun(r1, r2, n):
    i = 0
    b = ['']*n
    while i!=n-1:
        if b[i]!=1:
            if r1[i]>r2[i]:
                i=r1[i]
            else:
                i=r2[i]
            b[i]=1
        else:
            return 0
        print(b)
    return 1

    


r1 = [0,0,0,0,4]
r2 = [2,3,1,4,4]
print(fun(r1, r2, 5))

