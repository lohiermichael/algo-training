from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        best = 0
        best_buy = prices[0]
        potential_buy = prices[0]
        i = 1
        while i < len(prices):
            best = max(best, prices[i] - best_buy)

            potential_buy = min(potential_buy, prices[i])

            if prices[i] - potential_buy > best:
                best_buy = potential_buy
                best = prices[i] - best_buy
            i += 1
        return best


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
