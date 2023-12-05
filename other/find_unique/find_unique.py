def find_unique(L):
    x = 0
    for a in L:
        x ^= a
    return x


if __name__ == "__main__":
    L = [4, 3, 3, 4, 5, 1, 1]
    print(find_unique(L))
