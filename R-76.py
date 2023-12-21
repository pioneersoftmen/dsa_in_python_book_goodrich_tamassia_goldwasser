class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def is_same_list(x, y):
        ptr_x = x
        ptr_y = y

        while ptr_x != ptr_y:
            if ptr_x.next == x or ptr_y.next == y:
                return False
            ptr_x = ptr_x.next if ptr_x.next != x else y
            ptr_y = ptr_y.next if ptr_y.next != y else x

        return True