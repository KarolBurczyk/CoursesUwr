plik = open('lista9\wprawka6.txt').readlines()
drugie = open('Python\lista9\wprawka6 copy.txt').read()

t = {

}

for i in range(len(plik)-1):
    if plik[i][0]=='#':
        pass
    elif plik[i][0]=='+':
        plik[i] = plik[i].split()
        if plik[i][1] in t:
            t[plik[i][1]] += int(plik[i][2])
        else:
            t[plik[i][1]] = int(plik[i][2])
    else:
        plik[i] = plik[i].split()
        if plik[i][0] in t:
            t[plik[i][0]] = t[plik[i][0]] - int(plik[i][2])
        else:
            t[plik[i][0]] = -int(plik[i][2])
        if plik[i][1] in t:
            t[plik[i][1]] += int(plik[i][2])
        else:
            t[plik[i][1]] = int(plik[i][2])
m = 0
m_id = 0
for element in t:
    if t[element] > m:
        m = t[element]
        m_id = element

print(m_id, m) 

k = hash(drugie)
i = 0
while '7777777' not in str(k):
    k+=1
    i+=1
print('hash:', k, 'liczba na dzisiaj:', i)