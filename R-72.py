class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def concatenate_lists(L, M):
        if L is None:
            return M
        if M is None:
            return L
        
        current = L

        while current.next is not None:
            current = current.next

        current.next = M
        return L
    
# Example usage:

# Create the first linked list: 1 -> 2 -> 3-> None
L = Node(1)
L.next = Node(2)
L.next.next = Node(3)

# Create the second linked list: 4 -> 5 -> 6 -> None
M = Node(4)
M.next = Node(5)
M.next.next = Node(6)

# Concatenate the lists L and M 
concatenated = Node.concatenate_lists(L, M)

# Traverse the concatenated list and print the data of each node 
current = concatenated
while current is not None:
    print(current.data, end='')
    current = current.next