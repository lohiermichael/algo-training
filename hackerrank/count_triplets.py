from typing import *
import time

def count_power_until_next(arr: list, r: int, power: int, from_index: int) -> Tuple[int, int]:
    """
    Count the number of an element at a certain power until the next power
    Args:
        from_index: index from which we start to research
        arr: list in which in research is made
        r: element
        power: power

    Returns:
        count, index_last: The count of the element at this power and the index at which in appears the last
    """
    count = 0
    index_last = 0
    i = from_index
    while i < len(arr):
        if arr[i] == r ** power:
            count += 1
            index_last = i
        elif arr[i] == r ** (power + 1):
            break
        i += 1
    return count, index_last


def count_triplets_starts_with(r: int, power: int, arr: list):
    """
    Count the number of triplets that start with a given element
    Args:
        r: the element powered
        power: the power
        arr: the list in which in research is made

    Returns:
        count
    """
    count = 0
    index_start = 0
    while index_start < len(arr):
        if arr[index_start] == r ** power:
            count_1, index_last1 = count_power_until_next(arr=arr, r=r, power=power, from_index=index_start)
            count_2, index_last2 = count_power_until_next(arr=arr, r=r, power=power + 1, from_index=index_last1 + 1)
            count_3, _ = count_power_until_next(arr=arr, r=r, power=power + 2, from_index=index_last2 + 1)
            # if count_2 == 0 or count_3 == 0:
            #     break
            count += count_1 * count_2 * count_3
            index_start = index_last1 + 1
        else:
            index_start += 1

    return count


def count_triplet(arr, r):
    """
    Count the number of following triplets of consecutive powers of an integer in a list
    Args:
        arr: the list
        r: the integer

    Returns:
        int
    """
    count = 0
    power = 0
    maxi = max(arr)
    while r**(power+2) <= maxi:
        count += count_triplets_starts_with(r=r, power=power, arr=arr)
        power += 1
    return count


if __name__ == "__main__":
    L = [1, 3, 3, 9, 3, 9]
    print(L)
    s = time.time()
    print(count_triplet(L, 3))
    e = time.time()
    print(e-s)