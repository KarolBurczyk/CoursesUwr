class TreeItem:
    def __init__(self, value):
        self.val = value
        self.right = None
        self.left = None

t = TreeItem(10)
t.right = TreeItem(7)
t.left = TreeItem(1)

def s_odseparowane(t, s):
    if t.left!=None and t.right!=None:
        lewa = s_odseparowane(t.left,s)
        prawa = s_odseparowane(t.right,s)
    elif t.left!=None:
        return s_odseparowane(t.left,s)
    elif t.right!=None:
        return s_odseparowane(t.right,s)
    else:
        return [t.val, True]
    if  lewa[1]==True and prawa[1]==True:
        x = lewa[0] - prawa[0]
        zwrot = lewa[0] + prawa[0] + t.val
        if x<0:
            x=x*(-1)
        if x<=s:
            return [zwrot, True]
        else:
            return [0, False]
    else:
        return [0, False]

print(s_odseparowane(t, 7))