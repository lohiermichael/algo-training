from data_structure import ListNode

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    def mergeTwoListsRecursive(self, l1: ListNode, l2: ListNode) -> ListNode:
        def loop(l1, l2):
            if not l1:
                return l2
            elif not l2:
                return l1
            if l1.val <= l2.val:
                res = ListNode(l1.val)
                res.next = loop(l1.next, l2)
                return res
            elif l1.val > l2.val:
                res = ListNode(l2.val)
                res.next = loop(l1, l2.next)
                return res
        return loop(l1, l2)

    def mergeTwoListsIterative(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        #  Trick to initialize
        res = ListNode(0)
        node = res

        while l1 or l2:
            if (l1 and l2 and l1.val < l2.val) or (not l2):
                node.val = l1.val
                l1 = l1.next
            elif (l1 and l2 and l1.val >= l2.val) or (not l1):
                node.val = l2.val
                l2 = l2.next
            if l1 or l2:
                node.next = ListNode(0)
                node = node.next
        return res


if __name__ == "__main__":
    l1 = ListNode([1, 2, 4])
    l2 = ListNode([1, 3, 4])
    print(l1)
    print(l2)
    print(Solution().mergeTwoListsIterative(l1, l2))
