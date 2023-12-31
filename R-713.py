class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Create an empty list."""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size
    
    def is_empty(self):
        """Return True if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """Insert element e between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete non-sentinel node from the list and return its element."""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._prev = node._next = node._element = None
        return element
    
class PositionalList(_DoublyLinkedBase):
    """A sequential container of elements allowing positional access."""

    class Position:
        """An abstraction representing the location of a single element."""
        __slots__ = '_container', '_node'

        def __init__(self, container, node):
            """Constructor shouldn't be invoked by user."""
            self._container = container
            self._node = node

        def element(self):
            """Return the element stored at this Position."""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is Position representing the same location."""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """Return True if other does not represent the same location."""
            return not (self == other)

        def _validate(self, p):
            """Return position's node, or raise appropriate error if invalid."""
            if not isinstance(p, self.Position):
                raise TypeError("p must be proper Position type")
            if p._container is not self:
                raise ValueError("p doesn't belong to this number")
            if p._node._next is None:
                raise ValueError('p is no longer valid')
            return p._node


        def _make_position(self, node):
            """Return Position instance for given node (or None if sentinel)."""
            if node is self._header or node is self._trailer:
                return None
            else:
                return self.Position(self, node)

        def first(self):
            """Return the first Position in the list (or None if list is empty)."""
            return self._make_position(self._header._next)
        
        def last(self):
            """Return the last Positon in the list (or None if list is empty)."""
            return self._make_position(self._trailer._prev)


        def before(self, p):
            """Return the Position just before Position p (or None if p is first)."""
            node = self._validate(p)
            return self._make_position(node._prev)

        def after(self, p):
            """Return the Position just after Position p (or None if p is last)."""
            node = self._validate(p)
            return self._make_position(node._next)
        
        def __iter__(self):
            """Generate a forward iteration of the elements of the list."""
            cursor = self.first()
            while cursor is not None:
                yield cursor.element()
                cursor = self.after(cursor)

        def _insert_between(self, e, predecessor, successor):
            """Override inherited version to return Position, rather than Node."""
            node = super()._insert_between(e, predecessor, successor)
            return self._make_position(node)
        
        def add_first(self, e):
            """Insert element e at the front of the list and return new Position."""
            return self._insert_between(e, self._header, self._header._next)
        
        def add_last(self, e):
            """Insert element e at the back of the list and return new Position."""
            return self._insert_between(e, self._trailer._prev, self._trailer)
        
        def add_before(self, p, e):
            """Insert element e into list before Position p and return new Position."""
            original = self._validate(p)
            return self._insert_between(e, original._prev, original)

        def add_after(self, p, e):
            """Insert element e into list after Position p and return new Position."""
            original = self._validate(p)
            return self._insert_between(e, original, original._next)

        def delete(self, p):
            """Remove and return the element at Positon p."""
            original = self._validate(p)
            return self._delete_node(original)
        
        def replace(self, p, e):
            """Replace the element at Position p with e.
            Return the element formerly at Position p.
            """
            original = self._validate(p)
            old_value = original._element
            original._element = e
            return old_value
        
        def max(self):
            """Return the maximum element in the list."""
            if self.is_empty():
                raise ValueError("List is empty")
            max_element = self.first().element()
            cursor = self.first()
            while cursor is not None:
                if cursor.element() > max_element:
                    max_element = cursor.element()
                cursor = self.after(cursor)
            return max_element
        
        def find(self, e):
            """Return the Position of the first occurrence of element e in the list (or
            None if not found)."""
            cursor = self.first()
            while cursor is not None:
                if cursor.element() == e:
                    return cursor
                cursor = self.after(cursor)
            return None