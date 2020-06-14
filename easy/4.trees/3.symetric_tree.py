from data_structure import TreeNode

"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


def make_example_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)
    return root


def make_example_2():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.right = TreeNode(3)
    root.right.right = TreeNode(3)
    return root


class Solution:
    def helper(self, t1, t2):
        return (not t1 and not t2) or (t1.val == t2.val and self.helper(t1.left, t2.right) and self.helper(t1.right, t2.left))

    def isSymmetric(self, root: TreeNode) -> bool:
        return not root or self.helper(root.left, root.right)


if __name__ == "__main__":
    root_1 = make_example_1()
    print(Solution().isSymmetric(root_1))
