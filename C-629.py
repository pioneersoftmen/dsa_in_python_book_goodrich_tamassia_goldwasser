class Full(Exception):
    pass

class ArrayQueue:
    def __init__(self, maxlen=None):
        self.data = []
        self.maxlen = maxlen

    def enqueue(self, item):
        if self.maxlen is not None and len(self.data) == self.maxlen:
            raise Full("Queue is full")
        self.data.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.data.pop(0)
        else:
            raise Empty("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.data[0]

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)