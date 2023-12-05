from typing import List


"""
Note:
Assume we are dealing with an environment 
which could only store integers within the 
32-bit signed integer range: [−231,  231 − 1]. 
For the purpose of this problem, assume that your function 
returns 0 when the reversed integer overflows.

"""


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        if s[0] == '-':
            s = s[1:]
            rev_s = '-' + s[::-1]
        else:
            rev_s = s[::-1]
        res = int(rev_s)
        if abs(res) < 2**31:
            return int(rev_s)
        else:
            return 0


if __name__ == "__main__":
    x = -123
    print(Solution().reverse(x))
