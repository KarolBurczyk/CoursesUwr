f = []

def fibonacii(k,r):    
    f.append(1 % r)    
    f.append(1 % r)    
    for i in range(2,k+1):        
        f.append(((f[i-1] % r) + (f[i-2] % r)) % r)    
    print(f[k-1])        


fibonacii(5,4)
