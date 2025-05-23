def fun(a):
    if a%2==0:
        return a/2
    else:
        return a*3+1

def ile(a):
    i=0
    while a!=1:
        a=fun(a)
        i+=1
    return i

def mediana(list):
    if len(list)%2==1:
        return list[(len(list)-1)/2]
    else:
        return (list[int((len(list))/2)]+list[int((len(list)-2)/2)])/2

def poile(a,b):
    list=[]
    for i in range(a,b+1):
        print('energia ', i, ' wynosi ', ile(i))
        list.append(ile(i))
    list=sorted(list)
    srednia=sum(list)/(len(list))
    print('mediana wynosi: ', mediana(list))
    print('srednia wynosi: ', int(srednia))
    print('maks wynosi: ', list[len(list)-1])
    print('min wynosi: ', list[0])




poile(1,8)