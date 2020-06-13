from data_structure import LinkedList

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


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

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if self.val != node.val:
            return self.next.deleteNode(node)
        else:
            self.val = node.next.val
            self.next = node.next.next

    def make_list_node_from_node(self, node: int):
        node_list_node = self
        while node_list_node.val != node:
            node_list_node = self.next
        return node_list_node


if __name__ == "__main__":
    head = ListNode([4, 5, 1, 9])
    node = head.make_list_node_from_node(5)
    print(head)
    print(node)
    head.deleteNode(node)
    print(head)
