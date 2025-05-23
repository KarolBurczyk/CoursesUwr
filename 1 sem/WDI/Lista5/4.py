def g(n):
    if n == 2:
        return 1
    if n == 1:
        return 1
    if n == 0:
        return 1
    else:
        return g(n-1)+g(n-2)+g(n-3)

a = int(input('podaj n:'))
print(g(a))
    