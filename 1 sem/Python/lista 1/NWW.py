a = input()
b = input()
a=int(a)
b=int(b)
if b>a:
    c=a
    a=b
    b=c
n=2
r=1
o=1
while a!=1 or b!=1:
    if a%n == 0 :
        if b%n == 0:
            r=r*n 
            b=b/n 
            a=a/n 
        else : 
            o=o*n
            a=a/n 
    elif b%n == 0:
        b=b/n 
        o=o*n 
    else: n=n+1
print(r*o)
