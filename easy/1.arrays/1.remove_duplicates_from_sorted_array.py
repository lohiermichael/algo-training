# [0,0,1,1,1,2,2,3,3,4]
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case
        if len(nums) <=1:
            return len(nums) 

        # Initiate last_value
        last_value = nums[0]
        i = 1
        while i < len(nums):
            # Current value is equal to last_value
            if nums[i] == last_value:
                del nums[i]
            # Current value is different than last_value
            else:
                last_value = nums[i]
                i += 1
        return len(nums)


if __name__ == "__main__":
    example = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(Solution().removeDuplicates(example))
