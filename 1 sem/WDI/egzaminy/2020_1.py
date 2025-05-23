class TreeItem:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

t = TreeItem(1)
t.right = TreeItem(3)
t.left = TreeItem(4)

def wypisz_sciezke(t, x):
    len = 0
    def dlugosc(t, len):
        if t!= None:
            if dlugosc(t.right, len+1) > dlugosc(t.left, len+1):
                return int(len + 1) 
        else:
            return int(len)

    array = [None for i in range(dlugosc(t, len))]
    i=0
    def sciezka(t, x, array, i):
        if t == None:
            return 0
        array[i]==t.val
        if t.val == x:
            return 1
        else:
            sciezka(t.right(), x, array, i+1)
            sciezka(t.left(), x, array, i+1)
        return 0
    if sciezka(t, x, array) == 1:
        print(1, array)
    else:
        print(0)

wypisz_sciezke(t, 4)

        
