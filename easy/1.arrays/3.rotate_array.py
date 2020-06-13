from typing import List
# [1,2,3,4,5,6,7]


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)


if __name__ == "__main__":
    example = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    Solution().rotate(nums=example, k=k)
    print(example)
