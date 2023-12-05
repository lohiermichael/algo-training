from typing import Tuple, List

def find_missing_numbers_constant_space(array: List[int])-> Tuple[int, int]:
    # Calculate the sum of the elements of the array and the missing
    # values: s_tot
    n: int = len(array)
    s_tot: int = int((n+2) * (n+3) / 2)

    # Calculate the sum of the elements of the array: s_array
    s_array : int = 0
    for x in array:
        s_array += x

    # Calculate the the sum of the two missing elements: skl = k + l
    skl: int = s_tot - s_array

    # Calculate the average of the two missing elements: akl
    akl: int = int(skl / 2)

    # Calculate the sum of the elements inferior to the average of the missing
    # elements: s_inf_akl
    s_inf_akl : int = 0
    for x in array:
        if x <= akl:
            s_inf_akl += x

    # Calculate k
    k = skl - s_inf_akl

    # Calculate l
    l = skl - k

    return k, l


def find_missing_numbers_linear_space(array: List[int]) -> Tuple[int, int]:
    # Keep an array of flags (booleans): is_in_array so that
    # is_in_array[i] is True if i is in array
    # Let's initialize it with only False values
    n: int = len(array)
    is_in_array: List[int] = [False] * (n+3)
    # Let's feed it
    for element in array:
        is_in_array[element] = True

    # The results will be the False values of is_in_array
    results: list = []
    for x in range(1, n+3):
        if not is_in_array[x]:
            results.append(x)
    k, l = results[0], results[1]

    return k, l



if __name__ == '__main__':
    test_array: List[int] = [1, 6, 3, 5]
    k, l = find_missing_numbers_constant_space(array=test_array)
    print(k, l)
    k, l = find_missing_numbers_linear_space(array=test_array)
    print(k, l)
