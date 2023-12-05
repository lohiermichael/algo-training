from typing import *


def generate(numRows: int) -> List[List[int]]:
    def next_step(prev):
        res = [1]
        i = 1
        while i < len(prev):
            res.append(prev[i] + prev[i - 1])
            i += 1
        res.append(1)
        return res

    def loop(n):
        if n ==0:
            return []
        if n == 1:
            return [[1]]
        elif n == 2:
            return [[1], [1, 1]]
        else:
            Prev = loop(n - 1)
            return Prev + [next_step(Prev[-1])]

    return loop(numRows)


if __name__ == "__main__":
    print(generate(numRows=5))
