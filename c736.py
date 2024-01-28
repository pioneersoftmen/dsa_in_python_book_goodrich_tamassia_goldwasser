class DoublyLinkedListPositionalList:
    class _Node:
        def __init__(self, element, prev=None, next=None):
            self.element = element
            self.prev = prev
            self.next = next
    
    class Position:
        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node.element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self):
            self._header = None
            self._trailer = None
            self._size = 0

        def __len__(self):
            return self._size
        
        def is_empty(self):
            return self._size == 0
        
        def _insert_between(self, element, predecessor, successor):
            new_node = self._Node(element, prev=predecessor, next=successor)
            predecessor.next = new_node
            successor.prev = new_node
            self._size += 1
            return self.Positin(self, new_node)
        
        def _delete_node(self, node):
            predecessor = node.prev
            successor = node.next
            predecessor.next = successor
            successor.prev = predecessor
            self._size -= 1
            element = node.element
            node.prev = node.next = node.element = None
            return element
        
        def first(self):
            if self.is_empty():
                return None
            return self.Position(self, self.header)
        
        def last(self):
            if self.is_empty():
                return None
            return self.Position(self, self._trailer)

        def before(self, position):
            node = position._node.prev
            if node is self._header:
                return None
            return self.Position(self, node)
        
        def after(self, position):
            node = position._node.next
            if node is self._trailer:
                return None
            return self.Position(self, node)
        
        def add_first(self, element):
            if self.is_empty():
                new_node = self._Node(element)
                self._header = self._trailer = new_node
            else:
                new_node = self._insert_between(element, None, self._header)
            return new_node
        
        def add_last(self, element):
            if self.is_empty():
                new_node = self._Node(element)
                self._header = self._trailer = new_node
            else:
                new_node = self._insert_between(element, self._trailer, None)

        def add_before(self, position, element):
            node = position._node
            return self._insert_between(element, node._prev, node)
        
        def add_after(self, position, element):
            node = position._node
            return self._insert_between(element, node, node.next)
        
        def deleter(self, position):
            node = position._node
            return self._delete_node(node)