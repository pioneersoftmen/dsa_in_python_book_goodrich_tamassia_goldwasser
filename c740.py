import time 

class FavoriteListMTF:
    class _Node:
        def __init__(self, element):
            self.element = element
            self.prev = None
            self.next = None
            self.access_count = 0

    
    def __init__(self):
        self._head = None
        self._size = 0

    def _move_to_front(self, node):
        if node is not self._head:
            # Remove node from its current position
            node.prev.next = node.next
            if node.next is not None:
                node.next.prev = node.prev

            # Add node to the front
            node.next = self._head
            node.prev = None
            self._head.prev = node
            self._head = node

    def access(self, element):
        current = self._head
        while current is not None:
            if current.element == element:
                current.access_count += 1
                self._move_to_front(current)
                return
            current = current.next

        # Element not in the list, add it to the front
        new_node = self._Node(element)
        new_node.access_count += 1

        if self._head is not None:
            new_node.next = self._head
            self._head.prev  = new_node
        self._head = new_node

        self._size += 1

    def purge_inactive_elements(self, n):
        current = self._head
        current_time = time.time()

        while current is not None:
            if current.access_count == 0 or (current_time - current.access_count > n):
                next_node = current.next
                self._remove_node(current)
                current = next_node
            else:
                current = current.next
    
    def _remove_node(self, node):
        if node.prev is not None:
            node.prev.next = node.next
        else:
            self._head = node.next


        if node.next is not None:
            node.next.prev = node.prev

        self._size -= 1


