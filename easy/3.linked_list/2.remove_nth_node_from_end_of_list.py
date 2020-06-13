from data_structure import ListNode

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


def length(self):
    if self.val is None:
        return 0
    else:
        return self.next.length() + 1


ListNode.length = length


def removeNthFromEnd(self, n: int) -> ListNode:
    l = self.length()
    print(l)

    def loop(node, i):
        if i == l-n+1:
            node.val = node.next.val
            node.next = node.next.next
        else:
            loop(node.next, i+1)
    return loop(self, 1)


ListNode.removeNthFromEnd = removeNthFromEnd


class Solution:
    def removeNthFromEndOptimal(self, head: ListNode, n: int) -> ListNode:
        # Initialize fast and slow
        fast = head
        slow = head
        # Make the fast move n nodes ahead the slow
        for _ in range(n):
            fast = fast.next

        # Side case: if fast took over the end of the list
        # It means it is the case where you want to remove the n-th last element (aka the first one)
        if not fast.val:
            return head.next

        # Make fast and slow move until fast reaches the end of the list
        while fast.next.val:
            fast = fast.next
            slow = slow.next
        # Make slow skip the current node
        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    head = ListNode([1, 2, 3, 4, 5])
    print(head)
    n = 2
    print(Solution().removeNthFromEndOptimal(head, n))
