import math

def czypierwsza(a):
    c = int(math.sqrt(a))
    for p in range(2,c):
        if a%p==0:
            return 0
    return 1

l=0
s='7777777'

for i in range(1,999):
    if i < 10:
        k = s + '00' + str(i)
    elif i < 100:
        k = s + '0' + str(i)
    else:
        k = s + str(i)
    if czypierwsza(int(k))==1:
        print(k)
        l+=1

for i in range(1,99):
    if i < 10:
        k = s + '0' + str(i)
    else:
        k = s + str(i)
    for j in range(1,9):
        h = str(j) + k
        if czypierwsza(int(h))==1:
            print(h)
            l+=1

for i in range(1,9):
    k = s + str(i)
    for j in range(10,99):
        h = str(j) + k
        if czypierwsza(int(h))==1:
            print(h)
            l+=1

for i in range(100,999):
    k = str(i) +s
    if czypierwsza(int(k))==1:
        print(k)
        l+=1
            
print(l)
