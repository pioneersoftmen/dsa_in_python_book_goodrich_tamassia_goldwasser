def remove_all(stack):
    if not stack.is_empty():
        stack.pop()
        remove_all(stack)
    