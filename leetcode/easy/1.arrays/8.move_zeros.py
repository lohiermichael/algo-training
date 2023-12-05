from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        first_zero_i = len(nums)
        while i < first_zero_i:
            if nums[i] == 0:
                nums.pop(i)
                first_zero_i -= 1
                nums.insert(first_zero_i, 0)
            else:
                i += 1


if __name__ == "__main__":
    example = [0, 1, 0, 3, 12]
    solution = Solution().moveZeroes(example)
    print(example)
