from data_structure import TreeNode
from typing import List

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
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        depth_dict = self.store_by_depth(root, {}, 0)
        return self.convert_to_list(depth_dict)

    def store_by_depth(self, tree: TreeNode, depth_dict: dict, current_depth: int) -> List[List[int]]:
        if tree:
            self.store_by_depth(tree.left, depth_dict, current_depth+1)
            self.add_element_in_depth(depth_dict, tree.val, current_depth)
            self.store_by_depth(tree.right, depth_dict, current_depth+1)
        return depth_dict

    def add_element_in_depth(self, depth_dict: list, element: int, current_depth: int) -> None:
        if not current_depth in depth_dict.keys():
            depth_dict[current_depth] = [element]
        else:
            depth_dict[current_depth].append(element)

    def convert_to_list(self, depth_dict: dict) -> List[List[int]]:
        L = (max(depth_dict)+1) * [0]
        for i in range(len(L)):
            L[i] = depth_dict[i]
        return L


if __name__ == "__main__":
    root = make_example()
    print(Solution().levelOrder(root))
