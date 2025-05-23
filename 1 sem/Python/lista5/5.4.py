a = int(input('podaj a: '))
b = int(input('podaj b: '))

def erastotenes(a,b):
    
    list=[]

    for i in range(a, b+1):
        list.append(i)

    res=[]

    for i in range(b+1-a):
        liczba = list[i]
        if liczba != 0:
            res.append(liczba)
            i+=liczba
            while i<=(b-a):
                list[i]=0
                i+=liczba
    return(res)

def palindromy(a,b):
    list=erastotenes(a,b)
    res = []
    for element in list:
        if str(element) == str(element)[::-1]:
            res.append(element)
    return res


print(palindromy(a,b))
            

            
