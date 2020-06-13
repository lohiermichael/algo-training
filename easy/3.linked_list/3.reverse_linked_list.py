from data_structure import ListNode

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    def reverseListIterative(self, head: ListNode) -> ListNode:
        current = head
        stack = []
        while current.val:
            stack.append(current.val)
            current = current.next
        reverse = ListNode(stack.pop())
        current = reverse
        print(stack)
        while stack:
            current.next = ListNode(stack.pop())
            current = current.next
        return reverse


if __name__ == "__main__":
    head = ListNode([1, 2, 3, 4, 5])
    print(head)
    print(Solution().reverseListIterative(head))
