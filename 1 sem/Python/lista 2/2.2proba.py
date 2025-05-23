n = int(input('podaj n: '))
s = int(2*n+1)
print((s) * '*')
for i in range(0,s):
    if (s-2*i-4)>0:
        print('*' + i*' ' + '*' + (s-2*i-4)*' ' + '*' + i*' ' + '*')
    else:
        print('*' + (n-1)*' ' + '*' + (n-1)*' ' + '*')