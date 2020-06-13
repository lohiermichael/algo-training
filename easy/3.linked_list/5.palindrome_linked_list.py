from data_structure import ListNode

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        head_l = []
        while head:
            head_l.append(head.val)
            head = head.next

        return head_l == head_l[::-1]


if __name__ == "__main__":
    head = ListNode([1, 0, 1])
    print(head)
    print(Solution().isPalindrome(head))
