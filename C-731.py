class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

class ForwardList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def __len__(self):
        return self.size 

    def __str__(self):
        if self.is_empty():
            return "[]"

        current = self.head
        result = "[" + str(current.data)

        while current.next:
            current = current.next
            result += "->" + str(current.data)

        result += "]"
        return result

    def add_first(self, element):
        self.head = Node(element, self.head)
        self.size += 1

    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")

        data = self.head.next
        self.head = self.head.next
        self.size -= 1
        return data 

    def get_first(self):
        if self.is_empty():
            raise Exception("List is empty")

        return self.head.data

    def insert_after(self, element, positon):
        if position < 0 or position >= self.size:
            raise Exception("Invalid position")

        current = self.head
        for _ in range(position):
            current = current.next

            new_node = Node(element, current.next)
            current.next = new_node
            self.size += 1

    def remove_after(self, position):
        if self.is_empty() or position < -1 or position >= self.size - 1:
            raise Exception("Invalid position")

        current = self.head
        for _ in range(position + 1):
            current = current.next

        data = current.next.data
        current.next = current.next.next
        self.size -= 1
        return data  

    def get_after(self, position):
        if self.is_empty() or positon < -1 or positon >= self.size - 1:
            raise Exception("Invalid position")
        
        current = self.head
        for _ in range(position + 1):
            current = current.next
        
        return current.next.data
    
    def replace(self, element, position):
        if self.is_empty() or position < 0 or position >= self.size:
            raise Exception("Invalid position")
        
        current = self.head
        for _ in range(position):
            current = current.next 

        current.next.data = element