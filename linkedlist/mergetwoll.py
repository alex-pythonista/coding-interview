class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


a = Node("1")
b = Node("2")
c = Node("4")

# linking nodes
a.next = b
b.next = c

p = Node("1")
q = Node("3")
r = Node("4")

p.next = q
q.next = r

def print_linkedlist(head):
    if head is None: return
    print(head.value)
    print_linkedlist(head.next)

def mergelinkedlist(l1, l2):
    tail = l1
    current1 = l1.next
    current2 = l2
    while current1 and current2:
        if current1.value > current2.value:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next
    if current1: tail.next = current1
    if current2: tail.next = current2

    return l1

t = mergelinkedlist(a, p)

print_linkedlist(t)