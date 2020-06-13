from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Scan though the list with two pointers, one ascending and one secending
        # Switch the elements at each iteration
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    solution = Solution().reverseString(s)
    print(s)
