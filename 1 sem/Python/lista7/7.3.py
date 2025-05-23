def dzielnikipierwsze(n):
    t = []
    i=2
    while n>1:
        if n%i==0:
            t.append(i)
            while n%i==0:
                n=n/i
        else:
            i+=1
    return set(t)

print(dzielnikipierwsze(210))
