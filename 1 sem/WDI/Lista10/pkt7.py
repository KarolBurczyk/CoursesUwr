class ListItem:
    def __init__(self, value):
        self.val = value
        self.next = None

def split_list(head):
    if not head:
        return
    negative_head = None
    negative_tail = None
    positive_head = None
    positive_tail = None
    current = head
    while current:
        if current.val < 0:
            if not negative_head:
                negative_head = current
                negative_tail = current
            else:
                negative_tail.next = current
                negative_tail = current
        else:
            if not positive_head:
                positive_head = current
                positive_tail = current
            else:
                positive_tail.next = current
                positive_tail = current
        current = current.next
    positive_tail.next = None
    negative_tail.next = None
    return negative_head, positive_head

head = ListItem(-1)
lista = head
lista.next = ListItem(-2)
lista = lista.next
lista.next = ListItem(1)
lista = lista.next
lista.next = ListItem(2)
lista = lista.next
lista.next = ListItem(-3)


negative_head, positive_head = split_list(head)

print("Ujemne:")
while negative_head:
    print(negative_head.val)
    negative_head = negative_head.next

print("Dodatnie:")
while positive_head:
    print(positive_head.val)
    positive_head = positive_head.next

