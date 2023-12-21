class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def concatenate_lists(L, M):
        last_node_L = L.prev

        last_node_L.next = M.next
        M.next.prev = last_node_L

        M.prev.prev.next = last_node_L
        last_node_L.prev = M.prev.prev

        L.prev = M.prev

        return L