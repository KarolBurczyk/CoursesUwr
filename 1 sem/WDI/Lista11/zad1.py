import sys

class TreeItem:
    def __init__(self,value):
        self.val = value
        self.left = None
        self.right = None

def insert( root, nkey):
    if root==None: 
        return TreeItem(nkey)
    if nkey < root.val:
        root.left = insert(root.left, nkey)
    elif nkey > root.val:
        root.right = insert(root.right, nkey)
    return root

def write(root):
    if root!=None:
        write(root.left)
        print(root.val, end=' ')
        write(root.right)
    

'''
zad1

max dla 1,2,3,4,5,6,7 lub 7,6,5,4,3,2,1
min dla 4,2,6,3,5,1,7

najwieksza dlugosc drzewa będzie kiedy będziemy funkcje insert uruchamiac dla liczb w kolejnosci rosnacej lub malejacej

najmniejsza dlugsc drzewa bedzie kiedy bedziemy funckje insert uruchamiac dla i=k//2, i=(0+k//2)//2, i=(k//2+k)//2... itd 
'''

#zad2

def count_height(t):
    if t==None:
        return 0
    return (1 + max(count_height(t.left), count_height(t.right)))

        
#zad3

def count_items(t):
    if t==None:
        return 0
    return (1 + count_items(t.left) + count_items(t.right))

#zad4

def write_positive(root):
    if root!=None:
        write_positive(root.left)
        if root.val>=0:
            print(root.val, end=' ')
        write_positive(root.right)    

#zad5

def is_bst(t, mini, maksi):
    if t == None:
        return True
    if t.val <= mini:
        return False
    if t.val >= maksi:
        return False
    return is_bst(t.left, mini, t.val) and is_bst(t.right, t.val, maksi)

#zad6

def merge_trees(tree1, tree2):
    while tree2.left!=None:
        tree2 = tree2.left
    tree2.left = tree1

#zad7

def insert_while(t, nkey):
    while 1:
        if t.left==None and t.val>nkey:
            t.left = TreeItem(nkey)
            return t
        if t.right==None and t.val<=nkey:
            t.right = TreeItem(nkey)
            return t
        if nkey>t.val:
            t = t.right
        elif nkey<t.val:
            t = t.left
        else:
            return t


#zad8 

# def rotation(u, v):
#     if u != None and v != None:
#         u.left = v.right
#         v.left = u

#tree1
tree1 = TreeItem(-1)
for i in range(0,6):
    insert(tree1, i)

#tree2
tree2 = TreeItem(8)
for i in range(9,15):
    insert(tree2, i)

write(tree1)
print()
write(tree2)
print()

merge_trees(tree1, tree2)
write(tree2)
print()



write_positive(tree1)
print()
print(count_height(tree1))
print(count_height(tree2))

# rotation(tree1, tree1.left)
# write(tree1)
# print()
insert_while(tree1, 6)
write(tree1)
print()
print(is_bst(tree1, -sys.maxsize, sys.maxsize))