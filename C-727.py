class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def prepend(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            self._append_recursive(data, self.head)

    def _append_recursive(self, data, current_node):
        if current_node.next is None:
            current_node.next = Node(data)
        else:
            self._append_recursive(data, current_node.next)

    def __str__(self):
        if self.is_empty():
            return "Empty list"
        else:
            return self._str_recursive(self.head)
        
    def _str_recursive(self, current_node):
        if current_node is None:
            return ""
        else:
            return str(current_node.next) + "-" + self._str_recursive(current_node.next)
        
        