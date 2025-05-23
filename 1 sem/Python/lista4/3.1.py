import math

def czypierwsza(a):
    k = int(math.sqrt(a)) + 1
    for i in range(2,k):
        if a%i==0:
            return 0
    return 1

l=0

for i in range(100000):
    if czypierwsza(i)==1:
        if '777' in str(i):
            print(i)
            l+=1
print(l)