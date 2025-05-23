a=open("Python\lista9\kalorie.txt").read()
t=a.split('\n')
l=[]
n=0
i=0
while n<len(t):
    while t[n]!='' and n<len(t):
        i+=int(t[n])
        n+=1
    l.append(i)
    i=0
    n+=1
l = sorted(l)
a=int(l[len(l)-1])+int(l[len(l)-2])+int(l[len(l)-3])
print(a)


