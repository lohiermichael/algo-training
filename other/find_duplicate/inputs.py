from random import sample, shuffle, randrange


class InputFindDuplicate(list):
    def __new__(cls, n):
        """
        The input list will be of length n+1 with elements in {1..n}
        At max one of these elements will be duplicated
        Args:
            n: length of list - 1 or range of numbers of the input list
        """
        duplicate = randrange(1, n + 1)
        n_duplicates = randrange(2, (n + 1) // 2)
        L = sample(range(1, n), n + 1 - n_duplicates)
        L += n_duplicates * [duplicate]
        shuffle(L)
        return L


if __name__ == '__main__':
    # for i in range(100):
    #     test = InputFindDuplicate(10000)
    #     print(test)
    for i in range(100):
        test = InputFindDuplicate(n=6)
        print(test)
