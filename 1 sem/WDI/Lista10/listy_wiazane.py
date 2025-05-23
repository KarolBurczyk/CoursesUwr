class Listitem:
    def __init__(self, value):
        self.val = value
        self.next = None

def add_item(L, item):
    while L.next != None:
        L = L.next
    L.next = Listitem(item)

def extend(L,L1):
    while L.next != None:
        L = L.next
    L.next = L1

def print_list(L):
    while L.next != None:
        print(L.val, end=" ")
        L = L.next
    print(L.val)

def pop_element(L):
    previous = None
    while L.next != None:
        previous = L
        L = L.next
    del L
    previous.next = None

def remove_elements(L, n):
    previous = None
    while L.next != None:
        previous = L
        L = L.next
        if L.val == n:
            previous.next = L.next

def print_list_reversed(L):
    if L.next != None:
        print_list_reversed(L.next)
    print(L.val, end=" ")

def del_max(L):
    maks = L.val
    maks_id = None
    while L.next!=None:
        if L.next.val >= maks:
            maks = L.next.val
            maks_id = L
            print(maks)
            print(maks_id.val)
        L = L.next
    L = maks_id
    maks_id = maks_id.next
    maks_id = maks_id.next
    L.next = maks_id

def gdzieMax(L):
    maks_uno = L.val
    maks = L.val
    while L.next!=None:
        if L.next.val >= maks:
            maks = L.next.val
            maks_id = L.next
        L = L.next
    if maks == maks_uno:
        return 1
    if maks_id.next == None:
        return 1
    return 0


#L1 = Listitem(4)
L = Listitem(1)
##extend(L, L1)
add_item(L, 9)
add_item(L, 10)
add_item(L, 3)
add_item(L, 11)
#print_list(L)
#pop_element(L)
#remove_elements(L, 2)
#print_list_reversed(L)
# print_list(L)
# del_max(L)
# print_list(L)
print(gdzieMax(L))