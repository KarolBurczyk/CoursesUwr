class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    return prev

head = ListItem(1)
L = head
L.next = ListItem(2)
L = L.next
L.next = ListItem(3)
L = L.next
L.next = ListItem(4)
L = L.next
L.next = ListItem(0)

L = reverse_list(head)

while L:
    print(L.val, end=" ")
    L = L.next
