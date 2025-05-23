class Listitem:
    def __init__(self, value):
        self.val = value
        self.next = None
        self.last = self

def add_first_item(L, item):
    item = Listitem(L.val)
    L.val = item
    item.next = L.next
    L.next = item

def pop_first_item(L):
    L.val = L.next.val
    L.next = L.next.next

def add_last_item(L, item):
    item = Listitem(item)
    L.last.next = item
    L.last = item

def extend(L,L1):
    last = L1.last
    L1.last = None
    L.last.next = L1
    L.last = last

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


L = Listitem(5)
add_last_item(L, 6)
L1 = Listitem(4)
extend(L, L1)
#print_list(L)
#pop_element(L)
#remove_elements(L, 2)
print_list_reversed(L)
print_list(L)