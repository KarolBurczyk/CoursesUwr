def przeszukiwanie(n, X, s):
    def isfree(k, b[k]):
        for i in range(n):
            if b[i]==y:
                return 0
        return 1
    b = [-1]*n
    b[0]=0
    k=1
    while k<n and k>=0:
        b[k]+=1
    while b[k]<n and not isfree(k,b[k]):
        b[k]+=1
    if b[k]<n: k+=1
    else:
        b[k]=-1; k-=1
    return k


X = [[1,2,0,0,2], [1,1,2,1,0], [2,1,1,1,1], [1,1,1,2,1], [1,1,1,1,2]]
print(przeszukiwanie(5, X, 10))
        
    
        
                