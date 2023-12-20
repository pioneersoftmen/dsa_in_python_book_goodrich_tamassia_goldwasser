class ArrayDeque:
    def __init__(self):
        self.deque = []
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def size(self):
        return len(self.deque)
    
    def add_first(self, item):
        self.deque.insert(0, item)

    def add_last(self, item):
        self.deque.append(item)

    def remove_first(self):
        if self.is_empty():
            raise IndexError('Deque is empty.')
        return self.deque.pop(0)
    
    def remove_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.deque[0]
    
    def get_last(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.deque[-1]
    