from inputs import InputFindDuplicate


def floyd_algo(L):
    tortoise, hare = L[0], L[0]
    while True:
        tortoise = L[tortoise]
        hare = L[L[hare]]
        if tortoise == hare:
            break
    hare = L[0]
    while tortoise != hare:
        tortoise = L[tortoise]
        hare = L[hare]
    return tortoise


def sort_find(L):
    L_sorted = sorted(L)
    for i in range(len(L_sorted) - 1):
        if L_sorted[i] == L_sorted[i + 1]:
            return L_sorted[i]


def find_dict(L):
    encountered = set()
    for x in L:
        if x in encountered:
            return x
        else:
            encountered.add(x)


if __name__ == "__main__":
    L = [2, 6, 2, 3, 4, 1, 5, 2]
    for n in range(5, 1010, 10):
        for test in range(100):
            L_test = InputFindDuplicate(n=n)
            assert find_dict(L_test) == floyd_algo(L_test) == sort_find(L_test), \
                f"There is an issue with the list {L_test} "
        print(f"All is fine for n = {n}")

