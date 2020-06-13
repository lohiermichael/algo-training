from typing import List
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 1. Only keep the alphanumerical characters (keeping the uppercases)
        # 2. Change the string to a lower-case string
        s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return s == s[::-1]


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    print(Solution().isPalindrome((s)))
