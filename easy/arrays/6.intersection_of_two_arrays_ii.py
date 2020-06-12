from typing import List
from collections import Counter
from random import randint


# General case
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for x in set(nums1):
            res = res + min(nums1.count(x), nums2.count(x)) * [x]
        return res

    def intersect_sorted(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """In case nums1 and nums2 are sorted"""
        # Initiate the two iterators of nums1 and nums2
        i1, i2 = 0, 0
        res = []
        while i1 < len(nums1) and i2 < len(nums2):
            if nums1[i1] == nums2[i2]:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
        return res

    def intersect_chunks(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ In case you cannot load all num2 at once. The solution is to perform the algorithm by chunk """
        chunk_size = 3
        results = []
        # Perform the solutions by chunk
        for i in range(0, len(nums2), chunk_size):
            chunk = nums2[i: i+chunk_size]
            results.append(self.intersect(nums1, chunk))
        # For each element found in the results take keep it a number of time
        # equal to the minimum between the occurency in nums1 and the occurency in each of the chunks
        res = []
        for x in set(nums1):
            s = sum([res.count(x) for res in results])
            res = res + min(s, nums1.count(x)) * [x]
        return res


if __name__ == "__main__":
    # nums1 = [4, 9, 5]
    # nums2 = [9, 4, 9, 8, 4]
    # print(Solution().intersect(nums1, nums2))

    # sorted_num1 = [1, 2, 5, 5, 6, 10, 11]
    # sorted_num2 = [2, 2, 5, 10]
    # print(Solution().intersect_sorted(sorted_num1, sorted_num2))

    nums1 = [1, 2, 1, 1, 1, 3, 3, 3, 4, 4]
    big_nums2 = [randint(1, 10) for i in range(1000)]
    print(big_nums2)
    print(Solution().intersect_chunks(nums1, big_nums2))
    print(Solution().intersect(nums1, big_nums2))
