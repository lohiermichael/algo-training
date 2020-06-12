from typing import List
from collections import Counter


# General case
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in set(nums1):
            res = res + min(nums1.count(x), nums2.count(x)) * [x]
        return res


if __name__ == "__main__":
    nums1 = [4, 9, 5]
    nums2 = [9, 4, 9, 8, 4]
    print(Solution().intersect(nums1, nums2))
