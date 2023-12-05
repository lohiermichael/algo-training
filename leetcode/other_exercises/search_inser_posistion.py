from typing import *


def search_insert(nums: List[int], target: int) -> int:
    def loop(l, r):
        m = int((l + r) / 2)
        if l + 1 == r:
            if nums[l] >= target:
                return l
            elif nums[r] < target:
                return r + 1
            else:
                return r
        elif nums[m] > target:
            return loop(l, m)
        else:
            return loop(m, r)

    if len(nums) >= 2:
        return loop(0, len(nums) - 1)
    elif len(nums) == 1:
        if nums[0] < target:
            return 1
        else:
            return 0
    else:
        return 0


if __name__ == "__main__":
    print(search_insert([1, 3, 5, 6], 5))
