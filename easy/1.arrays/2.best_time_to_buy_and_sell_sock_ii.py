from typing import List
# [7,1,5,3,6,4]


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initiate variables
        profit = 0
        for i, x in enumerate(prices[1:], start=1):
            diff = x - prices[i-1]
            if diff > 0:
                profit += diff
        return profit


if __name__ == "__main__":
    example = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(example))
