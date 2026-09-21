class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        i, j = 0, 1
        while j < len(prices):
            max_profit = max(max_profit, max_profit + prices[j] - prices[i])
            i += 1
            j += 1

        return max_profit