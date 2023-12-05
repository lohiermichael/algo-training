from collections import defaultdict


def count_triplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k * r] += v2[k]
        v2[k * r] += 1
    return count


if __name__ == '__main__':
    L = [1, 3, 3, 9, 3, 9]
    print(count_triplets(L, 3))
