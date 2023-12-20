class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.next)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

# Count the nodes in the linked list
count = count_nodes(head)
print('Number of nodes in the list:', count)