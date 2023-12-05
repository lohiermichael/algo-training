from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # The trick is to fill the list from the end
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1

        # Only will be left the elements of nums2
        nums1[:n] = nums2[:n]


if __name__ == "__main__":
    nums1 = [-1, 0, 1, 1, 0, 0, 0, 0, 0]
    m = 4
    nums2 = [-1, 0, 2, 2, 3]
    n = 5
    Solution().merge(nums1, m, nums2, n)
    print(nums1)
