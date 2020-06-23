from typing import List

# [1, 2, 3, 1]


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        encountered = set()
        for x in nums:
            # Break if a duplicate is encountered
            if x in encountered:
                return True
            encountered.add(x)
        # After scanning through all the array no duplicate was encountered
        return False


if __name__ == "__main__":
    example = [1, 2, 3, 1]
    print(Solution().containsDuplicate(example))
