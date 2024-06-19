class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


a = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")

# linking nodes
a.next = b
b.next = c
c.next = d

def print_linkedlist(head):
    if head is None: return
    print(head.value)
    print_linkedlist(head.next)

def reverselist(head, prev=None):
    if head is None: return prev
    next = head.next
    head.next = prev
    return reverselist(next, head)

    # prev = None
    # current = head # A
    # while current:
    #     next = current.next # None
    #     current.next = prev # D.next = C
    #     prev = current # D
    #     current = next # None
        
    # return prev

print(reverselist(a).value)
