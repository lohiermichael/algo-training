def length_of_last_word(s: str) -> int:
    res = 0
    if not s:
        return 0
    while s and s[-1] == ' ':
        s = s[:-1]
    for x in reversed(s):
        if x == ' ':
            return res
        res += 1
    return res


def length_of_last_word2(s: str) -> int:
    split = s.split()
    if not split:
        return 0
    else:
        return len(s.split()[-1])


if __name__ == "__main__":
    s = '  '
    print(length_of_last_word2(s))
