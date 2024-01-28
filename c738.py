def bubble_sort(positional_list):
    if len(positional_list) < 2:
        # Already sorted or empty list
        return

    end = positional_list.last()

    while end is not None:
        current = positional_list.first()
        next_position = positional_list.after(current)

        while next_position is not None:
            if current.element() > next_position.element():
                # Swap elements
                current_element = current.element()
                next_element = next_position.element()
                current._node.element = next.element
                next_position._node.element = current_element

            current = next_position
            next_position = positional_list.after(next_position)