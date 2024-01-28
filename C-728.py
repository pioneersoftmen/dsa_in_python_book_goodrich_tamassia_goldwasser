class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

        # Existing methods...

    def reverse(self):
        self.head = self._reverse_recursive(self.head)

    def _reverse_recursive(self, current_node, prev_node=None):
        if current_node is None:
            return prev_node
        
        next_node = current_node.next
        current_node.next = prev_node

        return self._reverse_recursive(next_node, current_node)

linked_list = LinkedList()

linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(3)
linked_list.prepend(4)

print("Original List:", linked_list) # Output: 4 - 3 - 2 - 1
linked_list.reverse()
print("Reversed List:", linked_list) # Output: 1 - 2 - 3 - 4