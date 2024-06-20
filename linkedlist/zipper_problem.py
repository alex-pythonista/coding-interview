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

p = Node("P")
q = Node("Q")

p.next = q

def print_linkedlist(head):
    if head is None: return
    print(head.value)
    print_linkedlist(head.next)

def zipperlist(head1: Node, head2: Node):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0

    while current1 and current2:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        tail = tail.next

        count += 1
    
    if current1: tail.next = current1
    if current2: tail.next = current2

    return head1

lst = zipperlist(p, a)

print_linkedlist(lst)
