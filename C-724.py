class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node(None)


    def is_empty(self):
        return self.head.next is None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head.next
        self.head.next = new_node

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        
        popped_element = self.head.next.data
        self.head.next = self.head.next.next
        return popped_element
    
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        
        return self.head.next.data
    
    def size(self):
        count = 0 
        current = self.head.next

        while current is not None:
            count += 1
            current = current.next

        return count