def max(L):
    if len(L) == 0:
        raise ValueError("List is empty.")
    max_element = L.first().element() # Initialize max_element with the first element

    current_element = L.after(L.first()) # Start from the second element

    while current_element is not None:
        if current_element.element() > max_element:
            max_element = current_element.element()
        current_element = L.after(current_element)

    return max_element