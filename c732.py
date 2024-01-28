class CircularPositionalList:
    class _Node:
        def __init__(self, element, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next

    def __init__(self):
        self._header = self._Node(None)  # Dummy node for easy implementation
        self._size = 0
        self._cursor = self._header  # Cursor initially points to the header

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        new_node = self._Node(element, prev=predecessor, next=successor)
        predecessor.next = new_node
        successor.prev = new_node
        self._size += 1
        return new_node

    def add_first(self, element):
        if self.is_empty():
            new_node = self._Node(element)
            new_node.next = new_node
            new_node.prev = new_node
            self._header.next = new_node
            self._header.prev = new_node
            self._cursor = new_node
        else:
            self._insert_between(element, self._header, self._header.next)

    def add_last(self, element):
        if self.is_empty():
            self.add_first(element)
        else:
            self._insert_between(element, self._header.prev, self._header)

    def add_after_cursor(self, element):
        self._insert_between(element, self._cursor, self._cursor.next)

    def delete_first(self):
        if not self.is_empty():
            first_node = self._header.next
            self._header.next = first_node.next
            first_node.next.prev = self._header
            self._size -= 1
            if self._size == 0:
                self._cursor = self._header
            return first_node.element

    def delete_last(self):
        if not self.is_empty():
            last_node = self._header.prev
            self._header.prev = last_node.prev
            last_node.prev.next = self._header
            self._size -= 1
            if self._size == 0:
                self._cursor = self._header
            return last_node.element

    def delete_at_cursor(self):
        if not self.is_empty():
            current_node = self._cursor
            current_node.prev.next = current_node.next
            current_node.next.prev = current_node.prev
            self._cursor = current_node.next  # Move cursor to the next node
            self._size -= 1
            if self._size == 0:
                self._cursor = self._header
            return current_node.element

    def move_cursor_forward(self):
        if not self.is_empty():
            self._cursor = self._cursor.next

    def move_cursor_backward(self):
        if not self.is_empty():
            self._cursor = self._cursor.prev

    def get_cursor_element(self):
        return self._cursor.element

# Example Usage:
circular_list = CircularPositionalList()
circular_list.add_first(1)
circular_list.add_last(2)
circular_list.add_after_cursor(3)
circular_list.move_cursor_forward()
print("Current Cursor Element:", circular_list.get_cursor_element())
circular_list.delete_at_cursor()
print("List after deleting at cursor:", circular_list.__len__())  # Output: 2
