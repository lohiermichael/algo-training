class ListNode():
    def __init__(self, x):
        if isinstance(x, list):
            if not x:
                self.val = None
                self.next = None
            else:
                self.val = x[0]
                self.next = ListNode(x[1:])
        else:
            self.val = x
            self.next = None

    def __str__(self):

        if self.val is None:
            return 'None'
        return f"LinkedList({self.val}, {self.next.__str__()})"

    def make_list_node_from_node(self, node: int):
        node_list_node = self
        while node_list_node.val != node:
            node_list_node = self.next
        return node_list_node
