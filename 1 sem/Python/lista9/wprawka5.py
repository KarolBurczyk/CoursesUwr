a=open("Python\lista9\kalorie.txt").read()
t=a.split('\n')
n=1
i=0
m=0
while n<len(t)-1:
    while t[n]!='' and n<len(t)-1:
        i+=int(t[n])
        n+=1
    if i>m:
        m=i
    i=0
    n+=1
print(m)


