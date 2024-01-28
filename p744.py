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

        def __ne__(self, other):
            return not (self == other)
        def __init__(self):
            self._header = self._Node(None)
            self._trailer = self._Node(None)
            self._header.next = self._trailer
            self._trailer.prev = self._header
            self._size = 0


class TextEditor:
    def __init__(self):
        self.text = DoublyLinkedListPositionalList()  # Using a doubly linked list as the positional list
        self.cursor_position = self.text.first()  # Initialize cursor at the beginning

    def move_cursor_left(self):
        if self.cursor_position != self.text.first():
            self.cursor_position = self.text.before(self.cursor_position)

    def move_cursor_right(self):
        if self.cursor_position is not None and self.text.after(self.cursor_position) is not None:
            self.cursor_position = self.text.after(self.cursor_position)

    def insert_character(self, char):
        if self.cursor_position is not None:
            self.text.add_after(self.cursor_position, char)
            self.move_cursor_right()  # Move the cursor to the right after insertion

    def delete_character(self):
        if self.cursor_position is not None and self.text.after(self.cursor_position) is not None:
            deleted_char = self.text.delete(self.text.after(self.cursor_position))
            return deleted_char

    def display_text(self):
        current_position = self.text.first()
        while current_position is not None:
            print(current_position.element(), end="")
            current_position = self.text.after(current_position)
        print()
        if self.cursor_position is not None:
            cursor_index = self.text.position_index(self.cursor_position)
            underline = " " * cursor_index + "^"
            print(underline)

# Example Usage:
text_editor = TextEditor()

text_editor.insert_character('H')
text_editor.insert_character('e')
text_editor.insert_character('l')
text_editor.insert_character('l')
text_editor.insert_character('o')

text_editor.display_text()

text_editor.move_cursor_right()
text_editor.insert_character(' ')

text_editor.display_text()

text_editor.move_cursor_right()
text_editor.insert_character('W')
text_editor.insert_character('o')
text_editor.insert_character('r')
text_editor.insert_character('l')
text_editor.insert_character('d')

text_editor.display_text()

text_editor.move_cursor_left()
text_editor.delete_character()

text_editor.display_text()
