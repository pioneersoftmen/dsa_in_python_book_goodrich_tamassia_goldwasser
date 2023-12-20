def reverse_list(elements):
    stack = []
    for element in elements:
        stack.append(element)
    for i in range(len(elements)):
        elements[i] = stack.pop()