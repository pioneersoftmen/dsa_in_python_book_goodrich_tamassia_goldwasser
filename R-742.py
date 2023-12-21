def swap_nodes_doubly(x, y):
    if x == y:
        return
    
    if x.next == y:
        temp = x
        x = y
        y = temp

    prevX = x.prev
    nextX = x.next
    prevY = y.prev
    nextY = y.next

    if prevX is not None:
        prevX.next = y
    else:
        head = y

    if nextX is not None:
        next.prev = y

    if prevY is not None:
        prevY.next = x
    else:
        head = x

    x.next = nextY
    x.prev = prevY
    y.next = nextX
    y.prev = prevX

    
