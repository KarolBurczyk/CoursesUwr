import random
def kratka(N):
    for i in range(N):
        t = [0]*N
        for i in range(N):
            t[i] = random.randint(0,9)
        print('#'*(3*N+1))
        for j in range(2):
            for k in range(N):
                print('#'+str(t[k])+str(t[k]),end = '')
            print('#')
    print('#'*(3*N+1))


kratka(3)
        
