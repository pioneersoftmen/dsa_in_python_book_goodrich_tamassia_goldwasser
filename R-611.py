from collections import deque

class QueueAdapter:
    def __init__(self):
        self.items = deque()

    def is_empty(self):
        return len(self._items) == 0

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._items.popleft()

    def size(self):
        return len(self._items)
    
    def front(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._items[0]


    