from typing import List

# Given nums = [2, 7, 11, 15], target = 9


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        encountered = {}
        for i, x in enumerate(nums):
            if target - x in encountered.keys():
                return [encountered[target-x], i]
            encountered[x] = i


if __name__ == "__main__":
    nums = [2, 11, 15, 7]
    target = 9
    print(Solution().twoSum(nums, target))
