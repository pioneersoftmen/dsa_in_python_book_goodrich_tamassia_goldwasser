class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


def swap_nodes_singly(x, y, head):
    if x == y:
        return head

    prevX = None
    currX = head
    while currX is not None and currX.data != x:
        prevX = currX
        currX = currX.next

    prevY = None
    currY = head
    while currY is not None and currY.data != y:
        prevY = currY
        currY = currY.next

    if currX is None or currY is None:
        return head

    if prevX is None:
        head = currY
    else:
        prevX.next = currY

    if prevY is None:
        head = currX
    else:
        prevY.next = currX

    temp = currX.next
    currX.next = currY.next
    currY.next = temp

    return head