from data_structure import ListNode

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


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


ListNode.deleteNode = deleteNode


if __name__ == "__main__":
    head = ListNode([4, 5, 1, 9])
    node = head.make_list_node_from_node(5)
    print(head)
    print(node)
    head.deleteNode(node)
    print(head)
