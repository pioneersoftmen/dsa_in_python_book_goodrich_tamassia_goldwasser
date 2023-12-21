class Node:
    def __init__(self,data):
        self.data = data
        self.next= None
        self.prev = None

def find_middle_node(dllist):
    slow_ptr = dllist.next
    fast_ptr = dllist.next

    while fast_ptr.next is not None and fast_ptr.next.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr