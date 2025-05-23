slownik = open('sjp-20230129\slowa.txt', encoding="utf-8").read().split()
maks = ''
maks_count = 0
dic = {

}
for i in range(len(slownik)):
    if len(slownik[i])>=4:
        if slownik[i][len(slownik[i])-4:] in dic:
            dic[slownik[i][len(slownik[i])-4:]].append(slownik[i])
        else:
            dic[slownik[i][len(slownik[i])-4:]] = [slownik[i]]

for i in range(len(slownik)):
    if slownik[i].isalpha():
        a = slownik[i][:4]
        a = a[::-1]
        if a in dic:
            for j in range(len(dic[a])):
                if slownik[i]+dic[a][j] == (slownik[i]+dic[a][j])[::-1]:
                    print(slownik[i]+dic[a][j])
                    if len(slownik[i]+dic[a][j]) > maks_count:
                        maks = slownik[i]+dic[a][j]
                        maks_count = len(slownik[i]+dic[a][j])
print(maks, maks_count)
