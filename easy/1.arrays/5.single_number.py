from typing import List
from collections import Counter


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        c = Counter(nums)
        return min(c, key=c.get)


if __name__ == "__main__":
    example = [2, 2, 1]
    print(Solution().singleNumber(example))
