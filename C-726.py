class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    # Existing methods...

    def concatenate(self, Q2):
        if isinstance(Q2, LinkedQueue):
            if self.is_empty():
                self.head = Q2.head
                self.tail = Q2.tail
            else:
                self.tail.next = Q2.head
                self.tail = Q2.tail

            Q2.head = None
            Q2.tail = None

        else:
            raise TypeError("Q2 is not a LinkedQueue")