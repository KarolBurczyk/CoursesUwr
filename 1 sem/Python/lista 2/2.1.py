n = int(input('podaj n: '))
k = int(input('podaj k: '))
for i in range(n):
    for j in range(k):
        print(n*(k * ' ' + k  * '#'))
    for j in range(k):
        print(n*(k * '#' + k  * ' '))
