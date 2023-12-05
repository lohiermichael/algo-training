from typing import *


def max_sub_array(nums: List[int]) -> int:
    best = nums[0]
    i = 1
    while best < 0 and i < len(nums):
        if nums[i] > best:
            best = nums[i]
        i += 1
    s_inv = best
    for x in nums[i:]:
        s_inv += x
        if s_inv <= 0:
            s_inv = 0
        if s_inv > best:
            best = s_inv
    return best


def max_sub_array2(nums: List[int]) -> int:
    def loop(L):
        if len(L) == 1:
            return [L[0]]
        else:
            current = L.pop()
            Lr = loop(L)
            last = Lr[-1]
            return Lr + [max(current, last + current)]

    return max(loop(nums))


if __name__ == "__main__":
    nums = [1, 2, 3, -5]
    print(max_sub_array2(nums))
