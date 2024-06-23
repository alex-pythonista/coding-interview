class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


a = Node(3)
b = Node(0)
c = Node(-4)
d = Node(2)

# linking nodes
a.next = b
b.next = c
c.next = d
d.next = b

def iscycled(head):
    slow = fast = head #s = 3 f = 3 
        
    while fast and fast.next: # fast = 2 and f.next = 0
        slow = slow.next # -4
        fast = fast.next.next # 2
        if slow==fast: # 0 == 2
            return True

    return False

print(iscycled(a))