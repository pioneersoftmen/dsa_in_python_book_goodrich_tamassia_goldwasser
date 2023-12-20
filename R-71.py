class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

    def find_second_to_last(head):
        if head is None or head.next is None:
            return None # Handle empty or single-node list
        
        current = head
        prev = None

        while current.next is not None:
            prev = current
            current = current.next

        return prev
    
# Example usage:

# Create a linked list: 1 -> 2 -> 3 -> 4 -> None
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

second_to_last = Node.find_second_to_last(head)
if second_to_last is not None:
    print('Second-to-last node:', second_to_last.data)
else:
    print("No second-to-last node found")
