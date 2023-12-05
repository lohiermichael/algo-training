from data_structure import TreeNode
from math import inf

"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


def make_example_1():
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root


def make_example_2():
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return not root or self.helper(root, -inf, inf)

    def helper(self, tree, low, high):
        if not low < tree.val < high:
            return False
        if not tree.left and not tree.right:
            return low < tree.val < high
        elif not tree.left:
            return self.helper(tree.right, tree.val, high)
        elif not tree.right:
            return self.helper(tree.left, low, tree.val)
        else:
            return self.helper(tree.left, low, tree.val) and self.helper(tree.right, tree.val, high)


if __name__ == "__main__":
    root_1 = make_example_1()
    print(Solution().isValidBST(root_1))
    root_2 = make_example_2()
    print(Solution().isValidBST(root_2))
