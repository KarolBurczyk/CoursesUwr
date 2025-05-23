def k_element(X, n, k):
    if n==k and k==1:
        return X[0]
    m = 0
    mniejsze = ['']*(n)
    wieksze = ['']*(n)
    for i in range(n):
        if X[i]<X[0]:
            mniejsze[m-1]=X[i]
            m+=1
            print('mniejsze: ',X[i])
        elif X[i]>X[0]:
            wieksze[i-m-1]=X[i]
            print('wieksze: ',X[i])
    mniejsze[0]=X[0]
    wieksze[n-m-1]=X[0]
    print(wieksze)
    print(k)
    if m==k:
        return X[0]
    if m<k-1:
        k_element(wieksze,n-m, k-m)
    elif m>k-1:
        k_element(mniejsze,m, k)



X = [0,1,2,3,4,5,6,7,8,9]
n=10
k=4
print(k_element(X, n, k))
    