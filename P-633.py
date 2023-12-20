class ArrayDeque:
    def __init__(self, maxlen=None):
        self.maxlen = maxlen
        self.deque = []
    
    def is_empty(self):
        return len(self.deque) == 0
    
    def size(self):
        return len(self.deque)
    
    def append(self, item):
        if self.maxlen is not None and len(self.deque) == self.maxlen:
            self.deque.pop(0)
        self.deque.append(item)

    def appendleft(self, item):
        if self.maxlen is not None and len(self.deque) == self.maxlen:
            self.deque.pop()
        self.deque.insert(0, item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.deque.pop()

    def popleft(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.deque.pop(0)
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.deque[-1]
    
    def peekleft(sefl):
        if self.is_empty():
            raise IndexError("Deque is empty.")
        return self.deque[0]
    
    def remove(self, item):
        try:
            self.deque.remove(item)
        except ValueError:
            raise ValueError(f'{item} not in deque')