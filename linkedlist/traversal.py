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

output = []
def print_linkedlist(head):
    if head is None: return
    print(head.value)
    print_linkedlist(head.next)

# print(" -> ".join(output))


print_linkedlist(a)