from data_structure import ListNode

"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        hare = turtle = head
        while hare and turtle and hare.next:
            hare = hare.next.next
            turtle = turtle.next
            # Trick in case of no cycle to avoid the error message:
            # 'NoneType' object has no attribute 'val'
            if not hare:
                return False
            # Compare the values of the nodes as the nodes themselves will differ because we don't have real cycles
            if hare.val == turtle.val:
                return True
        return False


def make_cycle_list(L: list, pos) -> ListNode:
    """
    Almost make a circle list
    """
    node = ListNode(L[0])
    res = node
    pointer = 1
    count = 1
    # Add next node
    while count < 3*len(L):
        node.next = ListNode(L[pointer])
        node = node.next
        if pointer % len(L) == len(L)-1:
            pointer = pos
        else:
            pointer += 1
        count += 1
    return res


if __name__ == "__main__":
    test_true = make_cycle_list([3, 2, 4, 0], pos=1)
    print(Solution().hasCycle(test_true))
    test_false = ListNode([3, 2, 1, 0])
    print(Solution().hasCycle(test_false))
