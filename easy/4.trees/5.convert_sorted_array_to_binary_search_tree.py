from typing import List
from data_structure import TreeNode, Useful


"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if nums:
            nums_left, middle, nums_right = nums[:len(
                nums)//2], nums[len(nums)//2], nums[len(nums)//2+1:]
            tree = TreeNode(middle)
            tree.left = self.sortedArrayToBST(nums_left)
            tree.right = self.sortedArrayToBST(nums_right)
            return tree


if __name__ == "__main__":
    nums = [-10, -3, 0, 5, 9]
    tree = Solution().sortedArrayToBST(nums)
    print(Useful().levelOrder(root=tree))
