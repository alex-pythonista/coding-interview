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

print(a.next.value)
output = []
def print_linkedlist(head):
    if head is None: return
    print(head.value)
    print_linkedlist(head.next)

# print(" -> ".join(output))

# recursive varient
def findvalue(head, value):
    if head == None: return False
    if head.value == value: return True
    return findvalue(head.next, value)

print(findvalue(a, "B"))
print(findvalue(a, "A"))
print(findvalue(a, "F"))
print(findvalue(a, "C"))
print(findvalue(a, "D"))

# print_linkedlist(a)

def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    current = head
    while current and current.next:
        if current.value == current.next.value:
            current.next = current.next.next
            continue
        current = current.next

    return head

print()
