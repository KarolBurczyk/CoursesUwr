n = int(input('podaj n: '))
s = int(2*n+1)

def rek(i):
    if i<n-1:
        print('*' + i*' ' + '*' + (s-2*(i+2))*' ' + '*' + i*' ' + '*')
        rek(i+1)
        print('*' + i*' ' + '*' + (s-2*(i+2))*' ' + '*' + i*' ' + '*')
    else:
        print('*' + (n-1)*' ' + '*' + (n-1)*' ' + '*')

print((s) * '*')
rek(0)
print((s) * '*')
