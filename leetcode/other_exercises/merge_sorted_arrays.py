from typing import *


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    i1, i2, j = 0, 0, 0
    carry = []
    if nums1 and nums2:
        while i1 < m and i2 < n:
            if carry:
                if carry[0] <= nums2[i2]:
                    nums1[j] = carry.pop(0)
                    i1 += 1
                else:
                    carry.append(nums1[j])
                    nums1[j] = nums2[i2]
                    i2 += 1
            elif nums1[j] <= nums2[i2]:
                i1 += 1
            else:
                carry.append(nums1[j])
                i2 += 1
            j += 1

        while i2 < n:
            nums1[j] = nums2[i2]
            i2 += 1
            j += 1
        while carry:
            nums1[j] = carry.pop(0)
            j += 1
    elif not nums1:
        nums1[:] = nums2

    return nums1


if __name__ == "__main__":
    # nums1 = [4, 5, 6, 0, 0, 0]
    # nums2 = [1, 2, 3]

    # nums1 = [1]
    # nums2 = []

    # nums1 = [2, 0]
    # nums2 = [1]

    nums1 = [4, 0, 0, 0, 0, 0]
    nums2 = [1, 2, 3, 5, 6]
    print(merge(nums1=nums1, m=1, nums2=nums2, n=5))
