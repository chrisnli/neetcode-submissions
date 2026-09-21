class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        dp = defaultdict(lambda: float('inf'))

        for coin in coins:
            dp[coin] = 1

        for i in range(amount):
            for coin in coins:
                dp[i + coin] = min(dp[i + coin], dp[i] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1