from typing import List
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Get the Counter dictionary of the string
        counter = Counter(s)
        # Scan through s until the value of the key of the
        # current element in counter is equal to 1
        for i, x in enumerate(s):
            if counter[x] == 1:
                return i
        # In case no unique element was found
        return -1


if __name__ == "__main__":
    s = "loveleetcode"
    print(Solution().firstUniqChar(s))
