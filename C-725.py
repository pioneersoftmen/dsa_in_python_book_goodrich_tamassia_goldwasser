class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node(None)
        self.tail = self.head

    def is_empty(self):
        return self.head.next is None
    
    def enqueue(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        front_element = self.head.next.data
        self.head.next = self.head.next.next

        if self.head.next is None:
            # If the queue becomes empty after removal, update the tail as well
            self.tail = self.head

        return front_element
    
    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        
        return self.head.next.data
    
    def size(self):
        count = 0
        current = self.head.next

        while current is not None:
            count += 1 
            current = current.next

        return count