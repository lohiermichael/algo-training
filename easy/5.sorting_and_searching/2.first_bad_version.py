from random import randint

global n
global bad


def isBadVersion(k):
    return k >= bad


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high:
            mid = (high + low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low


if __name__ == "__main__":
    n = 1
    bad = 1
    sol = Solution().firstBadVersion(n)
    if bad == sol:
        print('ok')
