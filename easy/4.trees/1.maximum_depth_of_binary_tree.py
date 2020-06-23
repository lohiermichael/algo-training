from data_structure import TreeNode

"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


def make_example():
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def loop(tree):
            if not tree:
                return 0
            else:
                return max(loop(tree.left), loop(tree.right)) + 1
        return loop(root)


if __name__ == "__main__":
    # Same as on the Leetcode
    tree = make_example()
    print(Solution().maxDepth(tree))
