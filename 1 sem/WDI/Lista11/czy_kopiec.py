class TreeItem:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

t = TreeItem(2)
t.right = TreeItem(3)

def czy_kopiec(t):
    if t.right != None and t.left == None:
        return False
    if t.right == None and t.left != None:
        return False
    if t.right == None and t.left == None:
        return True
    if t.right.val < t.val or t.left.val < t.val:
        return False
    if czy_kopiec(t.right) and czy_kopiec(t.left):
        return True
    else:
        return False
    
     

print(czy_kopiec(t))
